# Breast Cancer Image Download and DICOM to PNG Conversion Project

This project is designed to automate the process of downloading breast cancer images from the internet and converting DICOM (.dcm) files to PNG format. It utilizes Python and provides two main functionalities:

1. **Downloading Images:** Web scraping techniques using Selenium and BeautifulSoup to gather images from target websites.
2. **Converting DICOM Files to PNG:** Using `pydicom` and `Pillow` libraries to standardize the images to 512x512 pixels in PNG format.

## Technologies Used
- **Python 3**: The main programming language of the project.
- **Selenium**: Used for web browser automation.
- **BeautifulSoup**: Used for parsing HTML content to extract data.
- **pydicom**: Used for processing DICOM files.
- **Pillow**: Used for image processing and resizing.

---

## Code Explanation

### 1. Image Download Script

The `download_images.py` script downloads images from a target URL and saves them into a designated folder.

- **Steps:**
  1. Launches the target webpage using Selenium.
  2. Scrolls the page to load more images.
  3. Collects image URLs and downloads them via HTTP.
  4. Saves the images into the `downloaded_images` folder with unique names to prevent overwriting.

- **Usage Tip:**
  The maximum number of images to download can be adjusted using the `max_images_to_download` variable. The script dynamically sets the starting index to prevent overwriting existing files in the folder.

---

### 2. DICOM to PNG Conversion Script

The `dcm_to_png.py` script converts all `.dcm` files in a specified folder to `.png` format and saves them into a designated output folder.

- **Steps:**
  1. Scans all `.dcm` files in the input folder.
  2. Reads and normalizes each DICOM file.
  3. Converts the normalized image to 8-bit format.
  4. Resizes the image to 512x512 pixels and saves it as a PNG file.

- **Usage Tip:**
  Input and output folders must be specified by the user. The script ensures the folders exist before processing.

---

## Requirements

To run this project, you need to have the following dependencies installed:
- Python 3.x
- `selenium`
- `beautifulsoup4`
- `pydicom`
- `Pillow`
- `webdriver-manager`

Install the dependencies using:
```
pip install selenium beautifulsoup4 pydicom pillow webdriver-manager
```

---

## Usage

### 1. Downloading Images
- Ensure the target URL is correctly set in the `download_images.py` script.
- Upon execution, images will be saved in a folder named `downloaded_images`.

### 2. DICOM to PNG Conversion
- Specify the input and output folders in the `dcm_to_png.py` script before execution.
- The output will be PNG images normalized and resized to 512x512 pixels.

---

## Important Notes
- Ensure compliance with the terms of use and data policies of the target website during web scraping.
- This project is intended for research and educational purposes only. It may not be suitable for commercial use.
