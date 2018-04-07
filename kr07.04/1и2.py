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
            c += 1
        if re.search("<se>",line):
            flag *= -1
    return c
 
def func_2(text):
    dict = {}
    for line in text:
        if re.search("[а-я]+", line, flags=re.IGNORECASE):
            j = 0
            l = re.search("gr=.+",line)
            for linne in text:
                if line == linne:
                    j += 1
            dict[l] = j
    return (dict)
 
writefile(str(func_1(readfile())))
writefile(str(func_2(readfile())))
