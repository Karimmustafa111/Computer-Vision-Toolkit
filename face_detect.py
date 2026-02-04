import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

print("The Camera is ON.. (Click 'q' to Exit)")

while True:
  success, img = cap.read()
  if not success:
    break

  gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

  faces = face_cascade.detectMultiScale(gray, 1.1, 4)

  for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.putText(img, "Karim", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

  cv2.imshow("Face Detector", img)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()