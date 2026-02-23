import cv2
image_path=r"C:\Users\HP\OneDrive\Pictures\image_3.jpg"
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

resized = cv2.resize(gray, None, fx=0.225, fy=0.35,interpolation=cv2.INTER_LINEAR)  #interpolation fn

h,w= resized.shape[:2]
center=(w//2,h//2)  #floor div
matrix = cv2.getRotationMatrix2D(center, angle=275, scale=1.0)
rotated = cv2.warpAffine(resized, matrix, (w,h))

edges=cv2.Canny(rotated, 100,150)


cv2.imshow("completed",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
