import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# img path
img = cv2.imread(r"cozy.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor=1.125,
                                      minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)


resized_img = cv2.resize(img, (int(img.shape[1]/7), int(img.shape[0]/7)))


cv2.imshow("Gray", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
