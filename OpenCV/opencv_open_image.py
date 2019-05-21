import cv2

img = cv2.imread("galaxy.jpg", 0)
""""
Options of what type of image
    rbg     has 3 bands
    1       with all the colors
    o       grayscale (has 2 band)
    -1      color image with transparency 
"""
# print(type(img))
# print(img)
# print(img.shape)
# print(img.ndim)

resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
#   resizing the image in order for it to fit the window
#   we will divide the shape aka the size of height and width by 2
cv2.imwrite("galaxy_resized.jpg", resized_image)
#   saving the resized image into an actual image
cv2.imshow("Galaxy", resized_image)
#   Creating a window to show the img and naming the window
cv2.waitKey(0)
#   Setting the time for the window to be loaded
cv2.destroyAllWindows()
#   After the time is elapsed then this will destroy all the windows
