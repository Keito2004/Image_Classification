import torch
import torchvision
import cv2

print("PyTorch:", torch.__version__)
print("TorchVision:",torchvision.__version__)
print("OpenCV:", cv2.__version__)

print("CUDA available:", torch.cuda.is_available())