import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#   create an object of the cascadeClassifier Class from the xml model

img = cv2.imread("photo.jpg")
#  when searching for faces grayscale tends to produce
#  higher accuracy fot better results
#  however we will load the image in rgb  first

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#   we convert the image to gray

faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor=1.05,
                                      minNeighbors=5)
#   we create a face object of the face_cascade to detect multi scale
#   this will take in the gray scale image, then the scale
#   that will enebale the xml model to search for the face.
#   the scale 1.05 means this will start searching for facial
#   structure at scale 1 and then reduce the image by 5% (0.05)
#   and minimum neighbours of 5


for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
#   we iterate over the faces for the begining of the face
#   at x,y,w,h and then draw a green box with a a border of 3
#   from the top ef x,y to x+width of face and y+height of face


print(type(faces))
print(faces)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
