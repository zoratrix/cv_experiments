from ultralytics import YOLO
import cv2

# Загружаем модель
model = YOLO("yolov8x.pt")  # самая лёгкая версия

# Камера
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow("Detection", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
