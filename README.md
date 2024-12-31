# Image Generation with CUDA

This application provides a graphical user interface (GUI) for generating images using the Stable Diffusion model. 
The GUI allows users to input a text prompt, and the application generates an image based on the prompt.

## Requirements
- Python 3.8 or higher
- `torch` library
- `diffusers` library
- `tkinter` library
- `customtkinter` library
- `Pillow` library
- GPU with CUDA support

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Ahmed5827/Image_Generation.git
   cd Image_Generation
   ```

2. Create a virtual environment and activate it:

   On Linux/MacOS:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Make sure you have a valid hugging face token in the file `Token.py` with the following content:

   ```python
   TOKEN = 'your_huggingface_token_here'
   ```

2. Run the application:

   ```bash
   python app.py
   ```

3. Enter your text prompt in the input field and click the **"Generate"** button. The application will display the generated image.

## Troubleshooting

- Ensure that your GPU supports CUDA and is properly configured.
- Verify that the `Token.py` file exists and contains a valid token for accessing the Stable Diffusion model.
- If you encounter any issues related to CUDA, make sure that your CUDA drivers and `torch` library are correctly installed and compatible.

## How It Works

1. The application uses `tkinter` and `customtkinter` for the GUI.
2. The text prompt entered by the user is processed using the Stable Diffusion model from the `diffusers` library.
3. The generated image is displayed directly in the GUI.
