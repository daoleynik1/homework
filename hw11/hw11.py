import re
 
def readfile(title):
    with open(title, "r", encoding="utf-8") as f:
        txt = f.read()
        return txt
 
def writefile(txt,title):
    with open(title, "w", encoding="utf-8") as f:
        f.write(txt)
    if not f.writable:
        print("Unable to get access to the end file.")
 
def substitute(txt):
    txt = re.sub('философия', 'астрология', txt)
    txt = re.sub('Философия', 'Астрология', txt)
    txt = re.sub('философии', 'астрологии', txt)
    txt = re.sub('Философии', 'Астрологии', txt)
    txt = re.sub('философией', 'астрологией', txt)
    txt = re.sub('Философией', 'Астрологией', txt)
    txt = re.sub('философий', 'астрологий', txt)
    txt = re.sub('Философий', 'Астрологий', txt)
    txt = re.sub('философию', 'астрологию', txt)
    txt = re.sub('Философию', 'Астрологию', txt)
    txt = re.sub('философиями', 'астрологиями', txt)
    txt = re.sub('Философиями', 'Астрологиями', txt)
    txt = re.sub('философиях', 'астрологиях', txt)
    txt = re.sub('Философиях', 'Астрологиях', txt)
    return txt
 
writefile(substitute(readfile(input("Enter in file name: "))), input ("Enter out file name: "))
