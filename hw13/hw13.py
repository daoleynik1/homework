import os

RUalphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ENalphabet = 'abcdefghijklmnopqrstuvwxyz'
#буквы других алфавитов не учитываются

def search_dirs(start_path):
    alldirs = []
    for root, dirs, files in os.walk(start_path):
        alldirs += dirs
    return alldirs

def find_max(alldirs):
    letters = {}
    for this_dir in alldirs:
        this_dir = this_dir.lower()
        if (this_dir[0] in RUalphabet) or (this_dir[0] in ENalphabet):
            if this_dir[0] in letters.keys():
                letters[this_dir[0]] += 1
            else:
                letters[this_dir[0]] = 1
    
    max_amount = -1
    max_letter = '' 
    for letter, amount in letters.items():
        if amount > max_amount:
            max_amount = amount
            max_letter = letter
            
    return max_letter

print('Чаще всего встречается буква ', end = '')
print(find_max(search_dirs('.')))