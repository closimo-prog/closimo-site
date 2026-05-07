import os
from PIL import Image

image_dir = r"d:\closimo\images"

for filename in os.listdir(image_dir):
    if filename.endswith(".png"):
        filepath = os.path.join(image_dir, filename)
        
        # Open the image
        img = Image.open(filepath)
        
        # Convert to RGB (in case it's RGBA)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')
        
        # Save as JPG with optimization
        jpg_filename = filename.replace(".png", ".jpg")
        jpg_filepath = os.path.join(image_dir, jpg_filename)
        
        # Compress and save as JPG
        img.save(jpg_filepath, 'JPEG', quality=85, optimize=True)
        print(f"Converted {filename} to {jpg_filename}")
        
        # Delete original PNG to avoid confusion
        os.remove(filepath)
        print(f"Deleted original {filename}")
