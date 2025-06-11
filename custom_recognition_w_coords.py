from ultralytics import YOLO
import cv2
import json

model = YOLO("best.pt")
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]  # берём 1й результат (для 1 кадра)

    detections = []
    for box in results.boxes:
        cls_id = int(box.cls[0])               # ID класса (число)
        class_name = model.names[cls_id]       # Название класса
        conf = float(box.conf[0])              # Уверенность
        x, y, w, h = box.xywh[0].tolist()      # Координаты bbox (центр x, y, ширина, высота)

        detections.append({
            "class": class_name,
            "confidence": round(conf, 3),
            "x": round(x, 1),
            "y": round(y, 1),
            "w": round(w, 1),
            "h": round(h, 1)
        })

    # Показываем bbox'ы
    annotated = results.plot()
    cv2.imshow("Detections", annotated)

    # Сохраняем координаты в JSON-файл по нажатию ENTER
    key = cv2.waitKey(1)
    if key == 13:  # Enter
        with open("bbox_snapshot.json", "w") as f:
            json.dump(detections, f, indent=2)
        print("✅ Сохранён bbox_snapshot.json")

    elif key == 27:  # Esc
        break

cap.release()
cv2.destroyAllWindows()
