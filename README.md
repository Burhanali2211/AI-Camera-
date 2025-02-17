# AI Camera with Object Detection and Audio Feedback

This project leverages YOLOv8 for object detection, EasyOCR for text recognition, and the Gemini API for scene description. It provides real-time audio feedback on the position of a person within a video frame to help them adjust their position while recording.

## Features:
- **Person Detection**: Uses YOLOv8 to detect a person in the frame.
- **Position Feedback**: Provides audio feedback about the person's position (e.g., "left", "center", "top") to help them adjust.
- **Text Recognition**: Recognizes and reads out any text detected in the frame using EasyOCR.
- **Real-time Scene Description**: Uses the Gemini API to generate a description of the scene including the person’s position and any detected text.

## Requirements:
Before running the app, make sure you have the following dependencies installed:

- Python 3.7 or higher
- YOLOv8 (ultralytics)
- EasyOCR
- pyttsx3
- Gemini API (Google)
- OpenCV
- numpy

### Install dependencies:

To set up the environment, open the terminal and run the following commands:

```bash
# Install required libraries
pip install opencv-python pyttsx3 easyocr google-generativeai ultralytics numpy
```

## Setup:

1. **Download YOLOv8 Weights:**
   - Download the YOLOv8 weights (`yolov8n.pt`) from the official [YOLO website](https://github.com/ultralytics/yolov8).
   - Place the weights in the same directory as the Python script or specify the path to it in the code.

2. **Gemini API Key:**
   - Replace the `GEMINI_API_KEY` in the code with your actual Gemini API key.

   ```python
   GEMINI_API_KEY = "your_api_key_here"
   ```

## Running the Application:

Once the dependencies are installed and the necessary files are set up, run the following command in your terminal to start the AI camera app:

```bash
python ai_camera.py
```

- The application will open a webcam feed and start detecting objects and text in the frame.
- If a person is detected, it will give audio feedback about their position (e.g., "The person is in the center of the frame").
- If text is detected, it will also be read aloud.
- Press `q` to exit the application.

## Usage:

- **Position Feedback**: When the app detects a person in the frame, it will tell you where they are, like "top left", "center", or "bottom right".
- **Text Recognition**: If any text appears in the frame, the app will read it out loud.
- **Scene Description**: The app uses the Gemini API to generate a scene description, including the position of the person and any detected text.

## Troubleshooting:

- **Webcam not working**: Ensure your webcam is properly connected and accessible. If you're using a virtual environment, check if the webcam is recognized.
- **Text not detected**: Make sure the text in the frame is clear and legible. The OCR might struggle with poorly lit or blurry text.
- **API errors**: Double-check your Gemini API key. If you encounter issues with the Gemini API, ensure your key is valid and not expired.

## License:

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments:

- **YOLOv8**: Used for real-time object detection.
- **EasyOCR**: Used for text recognition in images.
- **Gemini API**: Used to generate scene descriptions.
- **pyttsx3**: Used for text-to-speech conversion.

---

Feel free to fork or clone this repository and contribute to its improvement!

```

### Instructions:
1. **Install Dependencies**: Run the `pip install` command to install all the required Python libraries.
2. **Set Up YOLO Weights**: Make sure you have the `yolov8n.pt` weights in your project directory or update the path in the code.
3. **Replace Gemini API Key**: Replace the placeholder `your_api_key_here` with your actual Gemini API key.
4. **Run the App**: Use the terminal to run the Python script and start the real-time AI camera.

