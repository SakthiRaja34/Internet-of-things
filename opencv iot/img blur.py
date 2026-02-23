import cv2
image_path=r"C:\Users\HP\OneDrive\Pictures\image_3.jpg"
img = cv2.imread(image_path)  #0 for grayscale
resized = cv2.resize(img, None, fx=0.225, fy=0.35,interpolation=cv2.INTER_LINEAR)  #interpolation fn

# img = cv2.imread(image_path)
blur = cv2.GaussianBlur(resized,(9,9),0) #pass the resized img here

cv2.imshow("blured",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
