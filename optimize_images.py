import os
from PIL import Image

def optimize_images(directory):
    target_files = ['01.jpg', '02.jpg', '09.jpg', '10.jpg']
    for filename in os.listdir(directory):
        if filename in target_files:
            filepath = os.path.join(directory, filename)
            try:
                with Image.open(filepath) as img:
                    # Resize if very large (e.g., width > 1920)
                    if img.width > 1920:
                        ratio = 1920 / img.width
                        new_size = (1920, int(img.height * ratio))
                        img = img.resize(new_size, Image.Resampling.LANCZOS)
                    
                    # Save with optimization and lower quality
                    img.save(filepath, "JPEG", optimize=True, quality=80)
                    print(f"Optimized: {filename}")
            except Exception as e:
                print(f"Error optimizing {filename}: {e}")

if __name__ == "__main__":
    optimize_images("recursos")
