num = int(input('введите число:'))
x = 0
while x < num :
  x += 1
  word = input('введите слово:')
  if word == 'программирование':
    print('программа завершена')
    break
  else:
    print('ваше слово:', word)