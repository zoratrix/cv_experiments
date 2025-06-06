from ultralytics import YOLO
import torch
import cv2

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using device: {device}")

# Загружаем модель и указываем использование GPU
model = YOLO("yolov8x.pt")
model.to(device)

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, device=0, show=False)
    annotated = results[0].plot()
    cv2.imshow("Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
