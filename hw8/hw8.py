import random

filename = input("Input file name: ")
with open(filename, "r", encoding="utf-8") as f:
    h = f.read()
    h = h.split("\n")
    h = random.choice(h)
    h = h.split(" ")
    print(h [1], end = " ")
    for k in h[1]:
        print (".",end = "")
    print("\n")
    h = {h[0]: h[1]} 
    word = input("Please try to guess the word: ")
    while word not in h.keys():
        word = input("Please try again : ")
    print("Success!")
