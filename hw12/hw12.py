import re
import os

def xyz():
    file_list = os.listdir()
    return re.findall("[a-z]+\.[a-z]+", str(file_list), flags = re.IGNORECASE)

print(xyz())
print(len(xyz()))
print("В папке ",len(xyz )," файлов")
