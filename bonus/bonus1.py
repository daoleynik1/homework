number = 0
entered = []
while number != '':
    number = input('please enter a number: ')
    if number != '':
        try:
            number1 = float(number)
            entered.append(number1)
        except Exception:
            print('it doesnt look like a number :c')
else:
    mn = entered[0]
    mx = entered[0]
    su = 0
    for i in enumerate(entered):
        if i[1] <= mn:
            mn = i[1]
        if i[1] >= mx:
            mx = i[1]
        su += i[1]
        av = i[0] + 1
    average = su/av
    print('minimum number is ', mn)
    print('maximum number is ', mx)
    print('average is ', round(average, 4))
    print(entered)
    print(av)
