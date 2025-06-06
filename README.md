# cv_experiments
 Чтобы запустить на gpu:

 Для проверки выполнить в python:

'''
import torch
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
'''


Если torch.cuda.is_available() выдаёт False, тебе нужно установить PyTorch с поддержкой GPU.
Перейди на https://pytorch.org, выбери:
Stable, Pip, Python, CUDA 11.8 (или 12.1 — зависит от версии твоих драйверов)

У меня сработало:
'''
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
'''

Удалить и потом установить заново:

Удаляем текущую версию PyTorch
'''
pip uninstall torch torchvision torchaudio
'''
и затем установить снова (см версию выше)