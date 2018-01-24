import random
 
def simplesent5 ():
    sent = word("fullsent")
    return sent
 
def simplesent7():
    roll = random.random()
    if roll < 0.3:
        sent = word("noun3") + "は"+ word("verb3") + "。\n"
    elif roll > 0.7:
        sent = word("noun2") + "は"+ word("verb4") + "。\n"
    else:
        sent = word("noun4") + "は"+ word("verb2") + "。\n"
    return sent
 
def complexsentA():
    sent = word("timeplace") + "\n" + simplesent5() + "\n"
    return sent
 
def complexsentB():
    sent = word("affiction") + "の\n" + simplesent7() + "\n"
    return sent
 
def word(name):
    name = name +".txt"
    with open (name, "r", encoding = "utf-8") as f:
        res = f.read()
        res = res.split("\n")
        res = random.choice(res)
        return res
 
def make_haiku ():
    roll = random.random()
    if roll < 0.3:
        haiku = complexsentA() + simplesent7()
    elif roll > 0.7:
        haiku = simplesent7() + complexsentB()
    else:
        haiku = simplesent7() + simplesent5() + "\n" + simplesent7()
    return haiku
 
print(make_haiku())
