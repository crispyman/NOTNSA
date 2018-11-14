import face_recognition
#from faces import *
import cv2
import time
import glob
import numpy

known_face_encodings = []
known_face_names = []

for file in glob.glob("./profiles/*.npy"):
    known_face_encodings.append(numpy.load(file))
    # will break if you change directory name or file extention
    known_face_names.append(file[11:-4])

image = face_recognition.load_image_file("people.jpg")
display_image = image[:, :, ::-1]
face_locations = face_recognition.face_locations(image, model="cnn")
face_encodings = face_recognition.face_encodings(image, face_locations)

faces_names = []

for face_encoding in face_encodings:
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unkown"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
        print(name)

    faces_names.append(name)

for (top, right, bottom, left), name in zip(face_locations, faces_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 si$│    if True in matches:
    top *= 1
    right *= 1
    bottom *= 1
    left *= 1
    cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
    #cv2.rectangle(image, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(image, name, (left + 6, bottom + 10), font, 0.8, (255, 255, 255), 1)
    cv2.imshow('Video', display_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

while True:
    time.sleep(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

print(len(face_locations))
