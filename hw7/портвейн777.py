def ed(game):
    d = 0
    for word in game:
        if word[-2:] == 'ed':
            d = d+1
    return d
 
def ied(game):
    d = 0
    for word in game:
        if word[-3:] == 'ied':
            d = d+1
    return d
 
file = input("Enter the file title without txt ")
file += ".txt"
with open(file, "r", encoding='utf-8') as f:
    tekst = f.read()
    tekst = tekst.split(' ')
print("amount of words with 'ed': ", ed(tekst))
print("amount of words with 'ied': ", ied(tekst))
