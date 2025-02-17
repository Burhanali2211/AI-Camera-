import cv2
import pyttsx3
import easyocr
import google.generativeai as genai
from ultralytics import YOLO

# Load the YOLOv8 model (ensure you have the weights downloaded)
model = YOLO("yolov8n.pt")

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Adjust speech speed

# Initialize OCR reader
reader = easyocr.Reader(['en'])

# Gemini API Key (replace with your actual key)
GEMINI_API_KEY = "Your api key"
genai.configure(api_key=GEMINI_API_KEY)


def describe_scene(person_position, text):
    try:
        prompt = f"Tell me where the person is in the frame: {person_position}. Also, there is text: '{text}'."
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text if response else "No description available."
    except Exception as e:
        print(f"Error generating description: {e}")
        return "Error generating description."


def get_person_position(frame, results):
    # Find the 'person' class in the YOLO detection results
    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls)
            label = model.names.get(cls_id, "Unknown")
            if label == "person":  # If it's a person
                # Coordinates of the bounding box
                x1, y1, x2, y2 = box.xyxy[0].numpy()
                frame_center_x = frame.shape[1] // 2
                frame_center_y = frame.shape[0] // 2
                person_center_x = (x1 + x2) / 2
                person_center_y = (y1 + y2) / 2

                # Determine the position of the person in the frame
                if person_center_x < frame_center_x * 0.33:
                    x_position = "left"
                elif person_center_x > frame_center_x * 1.66:
                    x_position = "right"
                else:
                    x_position = "center"

                if person_center_y < frame_center_y * 0.33:
                    y_position = "top"
                elif person_center_y > frame_center_y * 1.66:
                    y_position = "bottom"
                else:
                    y_position = "middle"

                return f"The person is in the {y_position} {x_position} of the frame."
    return None


# Capture video from webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Run object detection
    results = model(frame)

    # OCR for text recognition
    text_result = reader.readtext(frame)
    detected_text = " ".join(
        [t[1] for t in text_result]) if text_result else ""

    # Get the position of the person
    person_position = get_person_position(frame, results)

    if person_position:
        scene_description = describe_scene(person_position, detected_text)
        print("Scene Description:", scene_description)
        engine.say(scene_description)
        engine.runAndWait()

    # Display the video feed with detections
    try:
        annotated_frame = results[0].plot()
        cv2.imshow("AI Camera", annotated_frame)
    except Exception as e:
        print(f"Error displaying frame: {e}")

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
