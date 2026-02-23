import cv2
image_path=r"C:\Users\HP\OneDrive\Pictures\image_3.jpg"
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges=cv2.Canny(gray,100,150)  #filter fn

cv2.imshow("EDGES",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
