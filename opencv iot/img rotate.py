import cv2
image_path=r"C:\Users\HP\OneDrive\Pictures\image_3.jpg"
img = cv2.imread(image_path)

if img is None:
    print("image not found")
else:
    print("img loaded successfully")

h,w= img.shape[:2]
center=(w//2,h//2)  #floor div

matrix = cv2.getRotationMatrix2D(center, angle=275, scale=1.0)
rotated = cv2.warpAffine(img, matrix, (w,h))

cv2.imshow("Rotated image",rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()