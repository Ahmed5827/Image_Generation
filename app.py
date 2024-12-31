import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk
from Token import TOKEN
import threading

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

# Create the app
app = tk.Tk()
app.geometry("532x700")
app.title("Stable Bud")
ctk.set_appearance_mode("dark")

# Create the prompt entry, using the correct font argument
prompt = ctk.CTkEntry(app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white")
prompt.place(x=10, y=10)

# Create the label for the generated image
lmain = ctk.CTkLabel(app, height=512, width=512)
lmain.place(x=10, y=110)

# Create the progress bar
progress_var = tk.DoubleVar()
progress_bar = ctk.CTkProgressBar(app, variable=progress_var, width=400)
progress_bar.place(x=66, y=650)  # Adjusted position

# Function to update the progress bar
def update_progress_bar():
    progress_var.set(0)  # Reset the progress bar
    for i in range(100):
        app.after(50)  # Pause for 50 milliseconds
        progress_var.set(i + 1)  # Increment the progress bar
        app.update_idletasks()

modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float32, use_auth_token=TOKEN)
pipe.to(device)

def generate():
    try:
        # Start the progress bar in a separate thread
        progress_thread = threading.Thread(target=update_progress_bar)
        progress_thread.start()

        # Run the Stable Diffusion pipeline to generate the image
        result = pipe(prompt.get(), guidance_scale=8.5)  # Run the pipeline
        print(result)  # Print the output to see its structure for debugging
        
        # Access the image correctly using the 'images' key
        image = result["images"][0]  # 'images' is the correct key in StableDiffusionPipelineOutput
        
        image.save('generatedimage.png')
        img = ImageTk.PhotoImage(image)
        lmain.configure(image=img)
        lmain.image = img  # Keep a reference to avoid garbage collection

    except Exception as e:
        print(f"An error occurred: {e}")

def start_generation_thread():
    # Run the generate function in a separate thread to keep the GUI responsive
    generation_thread = threading.Thread(target=generate)
    generation_thread.start()

# Create the generate button, using the correct font argument
trigger = ctk.CTkButton(app, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="blue", command=start_generation_thread)
trigger.configure(text="Generate")
trigger.place(x=206, y=60)

app.mainloop()
