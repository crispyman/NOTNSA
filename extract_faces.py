
from PIL import Image, ImageDraw
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("./people.jpg")

# Find all facial features in all the faces in the image
face_locations_list = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations_list)))
pil_image = Image.fromarray(image)

for face_locations in face_locations_list:

    # Print the location of each facial feature in this image
    #for facial_feature in face_landmarks.keys():
    #    print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

    # Let's trace out each facial feature in the image with a line!

    #pil_image.show()
    cropped_image = pil_image.crop((face_locations[3], face_locations[0], face_locations[1], face_locations[2]))

    cropped_image.show()

