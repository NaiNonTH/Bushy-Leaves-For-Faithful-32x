import os
import shutil

try:
    with open("./dest_dir.txt", "r") as reader:
        DEST_DIR = reader.read()
except FileNotFoundError:
    print("Please provide a \"dest_dir.txt\" file that contains a destination directory.")
    print("fail")
    exit(1)

shutil.copytree("./dist", os.path.join(DEST_DIR, "New Bushy Leaves for Faithful 32x"), dirs_exist_ok=True)
print("ok")