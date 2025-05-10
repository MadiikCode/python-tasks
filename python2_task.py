'''
1. Сортировка списка по чётности
Напишите программу, которая запрашивает список чисел у пользователя,
а затем:
сортирует чётные числа в порядке убывания,
нечётные — в порядке возрастания.

Условие:
    Пишем программу на основе функций

Пример:
    Ввод: 8, 3, 5, 2, 10
    Результат: [10, 8, 2, 3, 5]



def func_(numbers):
    evens =[]
    odd = []
    for i in numbers:
        if i % 2 == 0:
            evens.append(i)
        else:
            odd.append(i)
    return sorted(evens,reverse=True)+sorted(odd)

result = func_(list(map(int,input('Введите числа через пробел:').split())))
print(result)
'''

'''
Задача 2
Даны списка;

а = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
Нужно вернуть список который состоит из элементов общих для этих двух списков

#1
def qq_element(a,b):
    result = []
    for num in a:
        if num in b and num not in result:
            result.append(num)
    return result


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(qq_element(a,b))

#2
def common_elements(a, b):
    return [num for num in a if num in b]

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(common_elements(a, b))

#3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

s =[el for el in a if el in b]
print(s)
'''

'''
 Задача 3
 Найдите три ключа с самыми высокими значениями в словаре
 my_dict = {'a':500,'b':5874 'c':560,'d':400,'e':5874,'f':20}

#1
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}

top_keys = sorted(my_dict, key=my_dict.get, reverse=True)[:3]
print(top_keys)
#2


sorted(my_dict, key=my_dict.get, reverse=True)

sorted(my_dict) сортирует ключи словаря (по умолчанию сортировка идёт по алфавиту ключей, но мы указываем key=my_dict.get).
key=my_dict.get означает, что сортировка идёт по значениям.
reverse=True — делает сортировку по убыванию (чтобы самые большие значения были первыми).
[:3]

После сортировки берём первые три элемента — это и есть ключи с наибольшими значениями.
'''

'''
напишите функцию которая принимает 
строку и проверяет является ли строка палиндром
если является палиндромом то выйдет 

#1
word = 'level'
a = word[::-1]
if word == a:
  print("yes")
else:
  print("no")
#2
def func(word):
    return word == word[::-1]

print(func('level'))


#3

fsa = Lambda word:word == word[::-1]

#4
soz = input(':')
new = soz[::-1]....................
if soz == new:
print(true)
else:
print(false)
'''

'''
#Задача 4
#3
b = tuple(map(int,input('Введите число:').split(',')))
a = list(map(int,input('Введите число:').split(',')))
print(a)

#1
numbers = list(map(int,input(':').split()))
print(numbers)
#2
numbs_format_tuple = tuple(map(int,input('Введите числа:').split(',')))
numbs_format_list = tuple(map(int,input('Введи числа:').split(',')))

print(numbs_format_list)
print(numbs_format_tuple)
'''

'''
#Задача 5


#1
qqq = [1,2,3,4,5,6]
print(qqq[0])
print(qqq[-1])

qqq = [1,2,3,56,9]
print(f"Первое элемент :{qqq[0]}.Последний элемент: {qqq[-1]}")




def get_file_extension(file_name):
    file_parts = file_name.split(".")
    return file_parts[-1] if len(file_parts) > 1 else ""

# Пример использования
file_name = input("Введите имя файла: ")
extension = get_file_extension(file_name)

if extension:
    print(f"Расширение файла: {extension}")
'''

'''
задача 6
Вы принимаете от пользователя последовательность чисел, разделённых запятой. 
Составьте список и кортеж с этими числами.

#1
values = input('Введите числа через запятую: ')
ints_as_strings = values.split(',')
ints = map(int, ints_as_strings)
lst = list(ints)
tup = tuple(lst)
print('Список:', lst)
print('Кортеж:', tup)



#2
aq = input('Введите чисил разделенных запятой:')
aq.split(',')
numbers_list = [int(aq) for num in aq]
number_tuple = (numbers_list)

print(f'Список чисел {numbers_list}')
print(f"Список чисел {number_tuple}")
'''

'''
Задача 7
Напишите программу, которая принимает имя файла и выводит 
его расширение. Если расширение у файла определить невозможно, выбросите исключение.
#1
def get_file_extension(file_name):
    try:
        # Разделяем имя файла и расширение
        file_parts = file_name.split(".")
        # Проверяем, есть ли у файла расширение
        if len(file_parts) > 1:
            # Если есть, возвращаем последнюю часть
            return file_parts[-1]
        else:
            # Если расширение отсутствует, выбрасываем исключение
            raise ValueError("Файл не имеет расширения.")
    except Exception as e:
        # Ловим исключение и выводим сообщение об ошибке
        print(f"Ошибка: {e}")

# Пример использования
file_name = input("Введите имя файла: ")
extension = get_file_extension(file_name)
if extension:
    print(f"Расширение файла: {extension}")
#2
def get_extension(filename):
    filename_parts = filename.split('.')
    if len(filename_parts) < 2:  # filename has no dots
        raise ValueError('the file has no extension')
    first, *middle, last = filename_parts
    if not last or not first and not middle:
        # example filenames: .filename, filename., file.name.
        raise ValueError('the file has no extension')
    return filename_parts[-1]

print(get_extension('abc.py'))
print(get_extension('abc'))  # raises ValueError
print(get_extension('.abc'))   # raises ValueError
print(get_extension('.abc.def.'))   # raises ValueError
'''

'''
Задача 8
При заданном целом числе n посчитайте n + nn + nnn.


def gg(n):
    n1 = n
    n2 = int(str(n) ** 2)
    n3 = int(str(n) ** 3)
    return (n + n1 +n2)
print(gg(8))

#1
n = int(input("Введите число n: "))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
comp = n + int(t1) + int(t2)
print("Результат равен:", comp)
#2
n = input("Введите число: ")
result = int(n) + int(n * 2) + int(n * 3)
print("Результат:", result)

#3
def calculate_n_sum(n):
    n = str(n)
    return int(n) + int(n * 2) + int(n * 3)

num = int(input("Введите число: "))
print("Результат:", calculate_n_sum(num))

'''

'''
задача 9
отсортируйте словарь по значению в порядке возростанияя и убывания


result = {'a':3,'b':1'c':2}
w = sorted(result.values())
print(result)
'''
'''
numbs = [12,21,56,32,237,80,99]

for m in numbs:
    if m == 237:
       break

    elif m % 2== 0:
        print(m)
'''

