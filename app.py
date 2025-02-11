import streamlit as st
from pathlib import Path
from PIL import Image
import io
from rembg import remove
from constants import *


def remove_image(image_bytes, session):
    return remove(image_bytes, session=session)

# Streamlit app


def main():
    st.set_page_config(page_title="Image Removal Tool", page_icon=":camera:", layout="centered")

    st.title("Image Removal Tool")
    st.markdown("Upload your `.webp, .jpg , png` images to remove unwanted elements.")

    # File uploader
    uploaded_files = st.file_uploader("Upload .webp .png .jpg images", type=[
                                      "webp", "jpg", "png"], accept_multiple_files=True)

    if uploaded_files:
        st.write(f"Uploaded {len(uploaded_files)} file(s).")

        # Output directory

        Path(OUTPUT_PATH).mkdir(exist_ok=True)

        # Progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        image_grid = st.columns(3)  # Adjust the number of columns as needed
        grid_index = 0
        for i, uploaded_file in enumerate(uploaded_files):
            # Update progress
            progress = (i + 1) / len(uploaded_files)
            progress_bar.progress(progress)
            status_text.text(f"Processing {i + 1} of {len(uploaded_files)}: {uploaded_file.name}")

            # Read the uploaded file
            input_bytes = uploaded_file.read()

            # Process the image (replace `remove_image` with your actual function)
            output_bytes = remove_image(input_bytes, session=None)

            # Save the output image
            output_path = Path(OUTPUT_PATH) / (Path(uploaded_file.name).with_suffix(".out.png"))
            with open(output_path, "wb") as f:
                f.write(output_bytes)

            # Display the processed image
            with image_grid[grid_index]:
                st.image(Image.open(io.BytesIO(output_bytes)),
                         caption=f"Processed: {uploaded_file.name}", use_container_width=True)

            # Update grid index for the next image
            grid_index = (grid_index + 1) % len(image_grid)

        # Completion message
        st.success("Processing complete! Check the output folder for results.")
        st.markdown(f"**Output folder:** `{OUTPUT_PATH}`")


if __name__ == "__main__":
    main()
