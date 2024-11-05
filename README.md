# Background Removal using U²-Net

**Background Removal using U²-Net** is a web application that allows users to easily remove backgrounds from images using the state-of-the-art U²-Net deep learning model. The project leverages Flask as the web framework, providing a user-friendly interface for uploading images and retrieving background-free results.

## Features

- **Image Upload**: Users can upload images in various formats (JPEG, PNG, etc.) directly from their device.
- **Background Removal**: Utilizes the U²-Net model to accurately segment and remove backgrounds from the uploaded images.
- **Result Display**: The processed image with the background removed is displayed on the webpage and can be downloaded.
- **Responsive Design**: The web application is designed to be responsive, ensuring a seamless experience on both desktop and mobile devices.

## Technology Stack

- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **Deep Learning Model**: U²-Net for background removal
- **Image Processing**: OpenCV and PIL (Python Imaging Library)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Background-Removal-U2Net.git
   cd Background-Removal-U2Net
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the U²-Net model and place it in the `models` directory (see the repository for detailed instructions).

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Upload an image using the provided file input.
2. Click the "Remove Background" button to process the image.
3. View the resulting image with the background removed displayed on the same page.
