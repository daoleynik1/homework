word = list(input('Еnter a word: '))
for i,res in enumerate(word):
    res = "".join(word[-i:])
    res += "".join(word[:-i])
    print(res)
