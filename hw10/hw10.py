import re
 
def findlines(text):
    i = 1
    text = text.split("\n")
    for line in text:
        if re.search("Научная сфера",line):
            a = text[i]
            a = re.findall("[А-Я]+[а-я]+", a)
            break
        i += 1
    if a:
        return str(a)
 
fnamea = input("Файл статьи с расширением: ")
fnameb = input("Конечный файл с расширением: ")
 
with open(fnamea, "r", encoding="utf-8") as f:
    txt = f.read()
 
with open(fnameb, "w", encoding="utf-8") as f:
    f.write(findlines(txt))
if not f.writable:
    print("Не получилось открыть файл")
