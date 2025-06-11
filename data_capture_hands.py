import cv2
import os

# Папка для сохранения
save_dir = "dataset_hands"
os.makedirs(save_dir, exist_ok=True)

# Список шагов: (инструкция, имя класса)
steps = [
    ("Положи открытую ЛАДОНЬ в центр кадра", "hand_open"),
    ("Сожми ЛАДОНЬ в кулак", "hand_closed"),
    ("Захвати заготовку", "hand_grasp_workpiece"),
    ("Переноси заготовку слева направо", "hand_move_workpiece"),
    ("Отпусти заготовку", "hand_release_workpiece"),
    ("Захвати LID (крышку)", "hand_grasp_lid"),
    ("Переноси LID справа налево", "hand_move_lid"),
    ("Отпусти LID", "hand_release_lid"),
]

photos_per_step = 10  # сколько фото делать на каждый шаг

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("❌ Не удалось открыть камеру")
    exit()

print("\n🎬 ENTER — сделать фото | ESC — выйти\n")

for step_idx, (instruction, label) in enumerate(steps):
    print(f"\n📌 Шаг {step_idx + 1}/{len(steps)}: {instruction}")
    img_counter = 1

    while img_counter <= photos_per_step:
        ret, frame = cap.read()
        if not ret:
            print("❌ Ошибка чтения с камеры")
            break

        cv2.imshow("📷 Камера — нажми ENTER для снимка", frame)
        key = cv2.waitKey(1)

        if key == 13:  # Enter
            filename = f"{label}_{img_counter:02d}.jpg"
            filepath = os.path.join(save_dir, filename)
            cv2.imwrite(filepath, frame)
            print(f"✅ Сохранено: {filename}")
            img_counter += 1

        elif key == 27:  # ESC
            print("❌ Выход")
            cap.release()
            cv2.destroyAllWindows()
            exit()

cap.release()
cv2.destroyAllWindows()
print(f"\n🎉 Готово! Все фото сохранены в папке: {save_dir}")
