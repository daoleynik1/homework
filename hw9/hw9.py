import re
 
firstdoc = input('Введите имя исходного файла: ')
finaldoc = input('введите имя файла, в котором хотите видеть результат: ')
with open(firstdoc, "r", encoding="utf-8") as f:
    nov = f.read()
res = re.findall("вып[е]...[ \n.,?!]", nov) + re.findall("вып[ьи]..[ \n]", nov) + re.findall("вып[еьи].[ \n]", nov)
with open(finaldoc, "w", encoding="utf-8") as f:
    for word in res:
        if str(word.endswith('\n')):
            f.write(str(word[:-1])+" ")
        else:
            f.write(str(word)+" ")
if not f.writable:
    print("File is closed")
