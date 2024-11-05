#JAI SHRI RAM || JAI HANUMAN

import torch
import numpy as np
from PIL import Image
from torchvision import transforms
from models.u2net import U2NET  # Assume you've added the U²-Net model code in a folder called models

def load_model():
    model = U2NET(3, 1)  # Initialize U²-Net with input and output channels
    model.load_state_dict(torch.load("models/u2net.pth", map_location=torch.device("cpu")))
    model.eval()
    return model

def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((320, 320)),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225)),
    ])
    image = transform(image).unsqueeze(0)
    return image

def postprocess_mask(mask):
    mask = mask.squeeze().cpu().numpy()
    mask = (mask * 255).astype(np.uint8)
    mask = Image.fromarray(mask).resize((320, 320), Image.LANCZOS)
    return mask

def remove_background(model, image_path):
    # Load and preprocess image
    image = Image.open(image_path).convert("RGB")
    input_image = preprocess_image(image)
    
    # Generate the mask using the model
    with torch.no_grad():
        mask = model(input_image)[0][0]  # Assume U²-Net returns the mask as the first output

    # Process mask for transparency
    mask = postprocess_mask(mask)
    mask = mask.resize(image.size, Image.LANCZOS)
    
    # Apply mask to the original image
    image = image.resize(mask.size)
    image.putalpha(mask)  # Set the alpha channel to the mask
    
    # Save result
    result_path = image_path.replace("uploads", "uploads/results")
    image.save(result_path, "PNG")
    
    return result_path