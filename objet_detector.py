import cv2

cap = cv2.VideoCapture(0)

object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=False)

print("The System is ON.. Go in The Cadre and Prove! 🧍‍♂️")

while True:
  ret, frame = cap.read()
  if not ret:
    break

  mask = object_detector.apply(frame)

  _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
  contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  for contour in contours:
    if cv2.contourArea(contour) < 1500:
      continue

    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.putText(frame, f"Size: {w}x{h}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 255, 0), 2)
    
  cv2.imshow("Stationary Object Detector", frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()