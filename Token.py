import torch
print(torch.cuda.is_available())
print(torch.version.cuda)


print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version (PyTorch built with): {torch.version.cuda}")
print(f"Current CUDA device: {torch.cuda.current_device() if torch.cuda.is_available() else 'None'}")
print(f"Device name: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'None'}")



TOKEN="****"
