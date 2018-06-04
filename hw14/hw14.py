def custom_split(t, gran):
    chasti = [] #сделает так, чтобы сплит вернулся с войны
    eta_chast = ''
    for bus in t:
        if bus not in gran:
            eta_chast += bus # будет относиться к куску текста, если не сплитить
        else:
            # заикнет результат в список частей
            chasti.append(eta_chast)
            # обнулит нужный кусок текста
            eta_chast = ''
    return chasti
 
with open("ozhegov.txt", "r", encoding='utf-8') as f:
    t = f.read()
    t = custom_split(t, '.!?')
    dictionar = {sent: sent.split() for sent in t}
    for key, value in dictionar.items():
        dictionar[key] = {word: len(word) for word in key.split()}
    print('Словарь:', dictionar, sep='\n')
