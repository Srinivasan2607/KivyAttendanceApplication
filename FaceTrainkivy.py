import os
import face_recognition
import numpy as np

# Directory where your dataset is stored
dataset_dir = "D:\AttendanceVisualCode\dataset"

known_face_encodings = []
known_face_names = []

for person_dir in os.listdir(dataset_dir):
    person_path = os.path.join(dataset_dir, person_dir)
    if os.path.isdir(person_path):
        for image_filename in os.listdir(person_path):
            image_path = os.path.join(person_path, image_filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)
            if encoding:
                known_face_encodings.append(encoding[0])
                known_face_names.append(person_dir)

# Save the known_face_encodings and known_face_names to a file or database
np.save("known_face_encodings.npy", known_face_encodings)
np.save("known_face_names.npy", known_face_names)
