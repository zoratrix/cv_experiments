import cv2
import os

# === Классы и подварианты ===
workpieces = ['workpiece_red', 'workpiece_grey', 'workpiece_metal', 'workpiece_black']
lids = ['lid_grey', 'lid_blue', 'lid_green']

# === Сценарий шагов ===
steps = []

# 1. Заготовки по отдельности
for name in workpieces:
    for i in range(3):
        steps.append((f"📌 Поставь {name} на стол (вид сверху/сбоку)", name))
    for i in range(3):
        steps.append((f"📌 Возьми {name} в руку или частично закрой", name + "_hand"))

# 2. Крышки по отдельности
for name in lids:
    for i in range(3):
        steps.append((f"📌 Поставь {name} на стол", name))
    for i in range(3):
        steps.append((f"📌 Частично закрой {name} рукой", name + "_hand"))

# 3. Заготовка + крышка
for i in range(4):
    steps.append((f"📌 Положи заготовку и крышку рядом (любые цвета)", "workpiece_lid_combo"))

# 4. Несколько объектов
for i in range(4):
    steps.append((f"📌 Положи несколько заготовок и/или крышек, случайно", "multi_objects"))

# 5. Случайные перегруженные сцены
for i in range(10):
    steps.append((f"📌 Сцена с шумом / частично перекрытые объекты / беспорядок", "noisy"))

# === Папка для сохранения ===
save_dir = "dataset_capture_v2"
os.makedirs(save_dir, exist_ok=True)

# === Камера ===
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("❌ Не удалось открыть камеру")
    exit()

print("\n🎬 Нажимай ENTER для фото, ESC — выйти\n")

step_idx = 0
img_counter = {}

while step_idx < len(steps):
    instruction, label = steps[step_idx]
    print(f"\n👉 {instruction} ({step_idx+1}/{len(steps)})")

    if label not in img_counter:
        img_counter[label] = 1

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Ошибка чтения с камеры")
            break

        cv2.imshow("📷 Камера — нажми ENTER для снимка", frame)
        key = cv2.waitKey(1)

        if key == 13:  # ENTER
            filename = f"{label}_{img_counter[label]:02d}.jpg"
            filepath = os.path.join(save_dir, filename)
            cv2.imwrite(filepath, frame)
            print(f"✅ Сохранено: {filepath}")
            img_counter[label] += 1
            break
        elif key == 27:  # ESC
            print("❌ Выход")
            cap.release()
            cv2.destroyAllWindows()
            exit()

    step_idx += 1

cap.release()
cv2.destroyAllWindows()
print(f"\n🎉 Готово! Фото сохранены в: {save_dir}")
