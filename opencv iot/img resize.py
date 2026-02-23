import cv2
image_path=r"C:\Users\HP\OneDrive\Pictures\image_3.jpg"
img = cv2.imread(image_path)

if img is None:
    print("image not found")
else:
    print("img loaded successfully")

            #  cv2.resize(src,dsize,fx,fy,interpolation)
# resized = cv2.resize(img,(700,500))  #width,height
resized = cv2.resize(img, None, fx=0.225, fy=0.35,interpolation=cv2.INTER_LINEAR)  #interpolation fn
cv2.imshow("Resized Image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

