'''
#Обработка имени
try:
    hh= int(input(':'))
    print(hh)
except ValueError:
    print(';')


#Обратка сложений строкк
try:
    str_ = 'Madi'
    number = 3
    print(str_ + number)
except TypeError:
    print(';')


try:
    a = 2
    b = 0
    print(a / b)
except ZeroDivisionError:
    print(';')



try:
    m = (3,6,7)
    m[0] = 8
    print(m)
except TypeError:
    print(':')


try:
    login = input('Введите логин:')
    code = int(input('Введите пароль:'))

    if login == 'admin' and code == '123':
      print('Успешный вход:')
    else:
     print('Неверный пароль или логин')

except ValueError:
    print('Ошибка')

'''



while True:
    try:
       a = int(input('Первое числ:'))
       v = int(input('Второе числ:'))

       if v == 0:
           print('Нельзя делить на нол')
           continue
       print(f"Result: {a/v}")
       break

    except ValueError:
        print('Invalid input')