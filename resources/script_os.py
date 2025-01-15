import os.path

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, 'resources', "temp")

if not os.path.exists("temp"):
    os.mkdir("temp")

print(TMP_DIR)
print(CURRENT_FILE)
print(CURRENT_DIR)