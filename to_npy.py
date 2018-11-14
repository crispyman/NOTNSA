import face_recognition
import numpy
import glob

for file in glob.glob("./images/*.jpg"):
    image = face_recognition.load_image_file(file)
    # will break if you change directory name or file extention
    name = file[9:-4]
    #name = input("Enter Persons Name: ")
    image = face_recognition.face_encodings(image)[0]
    if name == "":
        name = "Known"
    numpy.save("./profiles/" + name, image)
    print(name)
