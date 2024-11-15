import os
import pydicom
from PIL import Image
import numpy as np

# These codes were written by utilizing various data processing training videos on the YouTube platform.
def dcm_to_png_batch(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".dcm"):
            dcm_path = os.path.join(input_folder, filename)
            png_filename = filename.replace(".dcm", ".png")
            png_path = os.path.join(output_folder, png_filename)
            
            dcm_data = pydicom.dcmread(dcm_path)
            img_array = dcm_data.pixel_array
            
            img_normalized = (img_array - img_array.min()) / (img_array.max() - img_array.min()) * 255.0
            img_normalized = img_normalized.astype(np.uint8)
            
            img = Image.fromarray(img_normalized)
            img = img.resize((512, 512), Image.LANCZOS)
            img.save(png_path)
            print(f"Saved as {png_path}.")

dcm_to_png_batch(r"C:\Users\namol\OneDrive\Desktop\dcm", r"C:\Users\namol\OneDrive\Desktop\png")
