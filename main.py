from cvzone.ClassificationModule import Classifier
import cv2
from pyfirmata import Arduino

# Initialize Arduino and pin configurations
port = 'COM7'
board = Arduino(port)
pin1, pin2, pin3, pin4 = 10, 11, 12, 13

# Initialize video capture
cap = cv2.VideoCapture(2)

# Load the classifier model
maskClassifier = Classifier('Resources/Model/keras_model.h5', 'Resources/Model/labels.txt')

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 50 and h > 50:  # Filter out small objects
            roi = img[y:y + h, x:x + w]
            predictions, index = maskClassifier.getPrediction(roi, draw=True)

            # Handle predictions for pins
            if index == 0:
                board.digital[pin4].write(1)  # Activate pin 4
            elif index == 0:
                board.digital[pin4].write(1)  # Activate pin 2
            elif index == 2:
                board.digital[pin3].write(1)  # Activate pin 3
            elif index == 3:
                board.digital[pin1].write(1)  # Activate pin 1
            else:
                # Deactivate all pins
                board.digital[pin1].write(0)
                board.digital[pin2].write(0)
                board.digital[pin3].write(0)
                board.digital[pin4].write(0)

            # Get label and draw rectangle
            label = maskClassifier.list_labels[index] if maskClassifier.labels_path else "Unknown"
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Image", img)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
