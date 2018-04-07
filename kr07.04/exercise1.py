import re

def readfile():
    with open("mystem.xml", "r", encoding="utf-8") as f:
        return f.read().split("\n")
 
def writefile(text):
    with open("mystemout.txt", "w", encoding="utf-8") as f:
        f.write(text)
    if not f.writable:
        print("Unable to get access to the end file.")
 
def func_1(text):
    c = 0
    flag = 1
    for line in text:
        if re.search("</se>",line):
            flag *= -1
        if flag == -1:
            print(line)
            c += 1
        if re.search("<se>",line):
            flag *= -1
    return c
 
writefile(str(func_1(readfile())))
