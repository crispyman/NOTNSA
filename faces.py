import face_recognition

known_face_encodings = []
known_face_names = []

andrew_image = face_recognition.load_image_file("Andrew.jpg")
andrew_face_encoding = face_recognition.face_encodings(andrew_image)[0]
known_face_encodings.append(andrew_face_encoding)
known_face_names.append("Andrew")


hayden_image = face_recognition.load_image_file("Hayden.jpg")
hayden_face_encoding = face_recognition.face_encodings(hayden_image)[0]
known_face_encodings.append(hayden_face_encoding)
known_face_names.append("Hayden")

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
known_face_encodings.append(biden_face_encoding)
known_face_names.append("Biden")

#peter_image = face_recognition.load_image_file("Peter.jpg")
#peter_face_encoding = face_recognition.face_encodings(peter_image)[0]
#known_face_encodings.append(peter_face_encoding)
#known_face_names.append("Peter")


wyatt_image = face_recognition.load_image_file("Wyatt.jpg")
wyatt_face_encoding = face_recognition.face_encodings(wyatt_image)[0]
known_face_encodings.append(wyatt_face_encoding)
known_face_names.append("Wyatt")


Hauns_image = face_recognition.load_image_file("Hauns.jpg")
Hauns_face_encoding = face_recognition.face_encodings(Hauns_image)[0]
known_face_encodings.append(Hauns_face_encoding)
known_face_names.append("Hauns")

# Create arrays of known face encodings and their names

