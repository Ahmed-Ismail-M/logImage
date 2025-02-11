# logImage - Background Remover UI

An open-source web application that allows users to remove backgrounds from multiple images using a simple drag-and-drop interface. Processed images are saved in an output folder, which can be configured from the constants file.

## Features
- Drag and drop multiple images for background removal.
- Automatic background removal using AI.
- Processed images are saved in the output folder.
- Configurable output directory via the `constants` file.

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- Required dependencies (listed in `requirements.txt`)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Ahmed-Ismail-M/logImage.git
   cd logImage
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application using Streamlit:
   ```sh
   streamlit run app.py
   ```

## Configuration
The default output folder for processed images is `output/`. You can modify this in the `constants.py` file:
```python
OUTPUT_FOLDER = "path/to/custom/output/folder"
```

## Usage
1. Launch the application.
2. Drag and drop images into the UI.
3. The application will process the images and remove their backgrounds.
4. Processed images will be saved in the `output/` folder (or the configured path).

## Acknowledgments
- Thanks to open-source rembg for background removal https://github.com/danielgatis/rembg?tab=readme-ov-file.
- Community contributors for enhancements and bug fixes.

---
For any questions or issues, feel free to open an [issue](https://github.com/Ahmed-Ismail-M/logImage/issues).