import cv2
image_path=r"C:\Users\HP\OneDrive\Pictures\image_3.jpg"
img = cv2.imread(image_path,0)  #0 for grayscale

_,thresh = cv2.threshold(img,127,255, cv2.THRESH_BINARY)

cv2.imshow("thresholded",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
