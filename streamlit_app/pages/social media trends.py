import streamlit as st
from pathlib import Path
from PIL import Image
from pinterest_scraper import *

def get_images_from_directory(directory):
    images = []
    for file in directory.iterdir():
        if file.suffix.lower() in ('.png', '.jpg', '.jpeg'):
            images.append(file)
    return images

st.title("Latest fashion trends from pinterest")
show_trends = st.checkbox("Show latest fashion trends from Pinterest")

if show_trends:
    st.write("Fetching and displaying fashion trends...")
    output = pinterest_images("fashion")
    fashion_images = []
    if output:
        current_directory = Path(__file__).resolve().parent
        pins_directory = current_directory.parent / "pins"
        fashion_images = get_images_from_directory(pins_directory)
        
    if fashion_images:
        st.write(f"Found {len(fashion_images)} fashion trend images:")
        for image_path in fashion_images:
            image = Image.open(image_path)
            st.image(image, caption=image_path.name, use_column_width=True)
    else:
        st.write("No fashion trend images found.")
