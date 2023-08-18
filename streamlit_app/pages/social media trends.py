import streamlit as st
import os
from PIL import Image
from pinterest_scraper import *

def get_images_from_directory(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            images.append(os.path.join(directory, filename))
    return images


st.title("Latest fashion trends from pinterest")
show_trends = st.checkbox("Show latest fashion trends from Pinterest")

if show_trends:
        st.write("Fetching and displaying fashion trends...")
        output = pinterest_images("fashion")
        fashion_images=[]
        if output:
            directory_path = os.path.abspath("pins")
            fashion_images = get_images_from_directory(directory_path)
        
        if fashion_images:
            st.write(f"Found {len(fashion_images)} fashion trend images:")
            for image_path in fashion_images:
                image = Image.open(image_path)
                st.image(image, caption=os.path.basename(image_path), use_column_width=True)
        else:
            st.write("No fashion trend images found.")


