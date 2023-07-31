import numpy as np
import os
import cv2
import face_recognition
import csv
import time


# Load the pre-trained Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

known_images_dir = "known"
known_image_paths = [os.path.join(known_images_dir, name) for name in os.listdir(known_images_dir)]
known_face_encodings = []
known_names = []

for image_path in known_image_paths:
    image = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(image)[0]  # Assuming only one face in the image
    known_face_encodings.append(face_encoding)
    known_names.append(os.path.splitext(os.path.basename(image_path))[0])

video_capture = cv2.VideoCapture(0)

# Create a CSV file for attendance
attendance_file = 'attendance.csv'
if not os.path.exists(attendance_file):
    with open(attendance_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Timestamp'])

recognized_faces = []
attendance_start_time = time.time()
attendance_duration = 7  # Set the duration (in seconds) for taking attendance

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Iterate over the detected faces
    for (x, y, w, h) in faces:
        # Extract the face region from the frame
        face_image = frame[y:y + h, x:x + w]

        # Resize the face image for better recognition performance (optional)
        face_image = cv2.resize(face_image, (0, 0), fx=0.25, fy=0.25)

        # Convert the face image to RGB for face recognition
        face_image_rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

        # Encode the face for recognition
        face_encoding = face_recognition.face_encodings(face_image_rgb)

        # Compare the face encoding with known faces
        if len(face_encoding) > 0:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding[0])
            name = "Unknown"

            # Find the best match among the known faces
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding[0])
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_names[best_match_index]
                recognized_faces.append(name)

            # Draw a rectangle around the face and display the name
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # Check if the attendance duration has passed
    elapsed_time = time.time() - attendance_start_time
    if elapsed_time >= attendance_duration:
        if recognized_faces:
            most_recognized_face = max(set(recognized_faces), key=recognized_faces.count)
            with open(attendance_file, 'a') as file:
                writer = csv.writer(file)
                writer.writerow([most_recognized_face, time.strftime('%Y-%m-%d %H:%M:%S')])

        # Reset the recognized faces and attendance start time
        recognized_faces = []
        attendance_start_time = time.time()

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the windows
video_capture.release()
cv2.destroyAllWindows()

# Print attendance report
with open(attendance_file, 'r') as file:
    reader = csv.reader(file)
    attendance_data = list(reader)

