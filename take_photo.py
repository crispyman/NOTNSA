from cv2 import *

cam = VideoCapture(0)
s, img = cam.read()
if s:
    namedWindow("cam-test",WINDOW_NORMAL)
    imshow("cam-test",img)
    waitKey(0)
    destroyWindow("cam-test")
    imwrite("./images/" + input("Enter your name") + ".jpg",img) #save image
