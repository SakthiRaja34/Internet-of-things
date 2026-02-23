import cv2
image_path=r"C:\Users\HP\OneDrive\Pictures\image_3.jpg"
img = cv2.imread(image_path)

if img is None:
    print("image not found")
else:
    print("img loaded successfully")

h,w,_ = img.shape
x1,y1 = 100,100
x2, y2 = 400,300
cropped = img[y1:y2,x1:x2]
cv2.imshow("cropped image",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()