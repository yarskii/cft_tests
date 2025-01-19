import os.path

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, "temp")

if not os.path.exists(TMP_DIR):
    os.makedirs(TMP_DIR)

print(f"Каталог TMP_DIR: {TMP_DIR}")
print(f"Существует ли каталог? {os.path.exists(TMP_DIR)}")
print(f"Доступен ли каталог для записи? {os.access(TMP_DIR, os.W_OK)}")
