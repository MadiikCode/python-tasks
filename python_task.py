"""
Задачи Tpproger:




# Задача 1
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
# Выведите все элементы, которые меньше 5.

#Самый простой вариант, который первым приходит на ум — использовать цикл for:

for elem in a:
    if elem < 5:
        print(elem)

#Также можно воспользоваться функцией filter, которая фильтрует элементы согласно заданному условию:

print(list(filter(lambda elem: elem < 5, a)))

#И, вероятно, наиболее предпочтительный вариант решения этой задачи — списковое включение:

print([elem for elem in a if elem < 5])




# Задача 2
# Даны списки:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
#
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
#
# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

#Можем воспользоваться функцией filter:

result = list(filter(lambda elem: elem in b, a))

#Или списковым включением:

result = [elem for elem in a if elem in b]

#А можно привести оба списка к множествам и найти их пересечение:

result = list(set(a) & set(b))



# Задача 3
# Отсортируйте словарь по значению в порядке возрастания и убывания.

#Импортируем нужный модуль и объявляем словарь:

import operator
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

#Сортируем в порядке возрастания:

result = dict(sorted(d.items(), key=operator.itemgetter(1)))

#И в порядке убывания:

result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))



# Задача 4
# Напишите программу для слияния нескольких словарей в один.

#Допустим, вот наши словари:

dict_a = {1:10, 2:20}
dict_b = {3:30, 4:40}
dict_c = {5:50, 6:60}

#Объединить их можно вот так:

result = {}
for d in (dict_a, dict_b, dict_c):
    result.update(d)





# Задача 5
# Найдите три ключа с самыми высокими значениями в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.

#Можно воспользоваться функцией sorted:

result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]

#Аналогичный результат можно получить с помощью функции nlargest из модуля heapq:

from heapq import nlargest
result = nlargest(3, my_dict, key=my_dict.get)




# Задача 6
# Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления.


print(int('ABC', 16))





# Задача 7
# Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на вершине и по бокам стоят единицы, а каждое число внутри равно сумме двух расположенных над ним чисел.

def pascal_triangle(n):
   row = [1]
   y = [0]
   for x in range(max(n, 0)):
      print(row)
      row = [left + right for left, right in zip(row + y, y + row)]

pascal_triangle(6)





# Задача 8
# Напишите проверку на то, является ли строка палиндромом. Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.

Тут всё просто, достаточно сравнить строку с её обратной версией, для чего можно использовать встроенную функцию reversed:

def is_palindrome(string):
    return string == ''.join(reversed(string))

print(is_palindrome('abba'))


#Того же эффекта можно добиться с помощью срезов:

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome('abba'))



# Задача 9
# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.

def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')

convert(1234565)



# Задача 10
# Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.

values = input('Введите числа через запятую: ')
ints_as_strings = values.split(',')
ints = map(int, ints_as_strings)
lst = list(ints)
tup = tuple(lst)
print('Список:', lst)
print('Кортеж:', tup)




# Задача 11
# Выведите первый и последний элемент списка.

lst = [1, 2, 3, 4, 5]
print(f'Первый: {lst[0]}; последний: {lst[-1]}')



#Задача 12
#Напишите программу, которая принимает имя файла и выводит его расширение. Если расширение у файла определить невозможно, выбросите исключение.

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

# Задача 13
# При заданном целом числе n посчитайте n + nn + nnn.



def solve(n):
    n1 = n
    n2 = int(str(n) * 2)
    n3 = int(str(n) * 3)
    print(n1 + n2 + n3)

solve(5)




# Задача 14
# Напишите программу, которая выводит чётные числа из заданного списка и останавливается,если встречает число 237.

numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
]

for x in numbers:
    if x == 237:
        break
    elif x % 2 == 0:
        print(x)



# Задача 15
# Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.

set_1 = set(['White', 'Black', 'Red'])
set_2 = set(['Red', 'Green'])

print(set_1 - set_2)



# Задача 16
# Выведите список файлов в указанной директории.

from os import listdir
from os.path import isfile, join
files = [f for f in listdir('/home') if isfile(join('/home', f))]
print(files)



#Задача 17
#Сложите цифры целого числа.

def sum_digits(num):
    digits = [int(d) for d in str(num)]
    return sum(digits)

print(sum_digits(5245))




#Задача 18
#Посчитайте, сколько раз символ встречается в строке.

string = 'Python Software Foundation'
string.count('o')




#Задача 19
#Поменяйте значения переменных местами.

x = 5
y = 10
x, y = y, x



#Задача 20
#С помощью анонимной функции извлеките из списка числа, делимые на 15.

nums = [45, 55, 60, 37, 100, 105, 220]
result = list(filter(lambda x: not x % 15, nums))



#Задача 21
#Нужно проверить, все ли числа в последовательности уникальны.

def all_unique(numbers):
    return len(numbers) == len(set(numbers))



#Задача 22
#Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.


text = 'lorem ipsum dolor sit amet amet amet'
words = text.split()
counter = collections.Counter(words)
most_common, occurrences = counter.most_common()[0]

longest = max(words, key=len)

print(most_common, longest)

"""

'''
f = {'два': 2,'один': 1,'трри': 3}

s = sorted(f,key=f.get)
print(s)




 1. FizzBuzz с модификацией: Напишите программу, которая выводит числа от 1 до 100.
Для чисел, кратных 3, выводите “Fizz”, для кратных 5 — “Buzz”, а для кратных 3 и 5 — “FizzBuzz”   


#1

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    if i % 3 == 0:
        print('Fizz')
    if i % 5 == 0 :
        print('Buzz')
    else:
        print(i)



#Как это работает?

#Если число делится и на 3, и на 5 — печатаем "FizzBuzz".
#Если только на 3 — "Fizz".
#Если только на 5 — "Buzz".
#В остальных случаях печатаем само число.

#2
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Вызываем функцию для чисел от 1 до 100
fizzbuzz(100)


#Теперь у нас есть функция fizzbuzz(n), которая принимает число n и выполняет FizzBuzz
# для диапазона от 1 до n.
#Можно легко поменять n, если захочешь проверить другой диапазон.




2. Анаграмма: Напишите функцию, которая проверяет, являются ли две строки анаграммами.

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# Пример использования
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False


#sorted(s1) и sorted(s2) сортируют буквы в строках.
#Если отсортированные версии одинаковые, значит, строки — анаграммы.



3. Частотный словарь: Напишите функцию, которая подсчитывает
количество каждого символа в строке.


#1
s = 'Hello,madi!'
m = len(s)
print(m)

#2
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Пример использования
print(char_frequency("hello world"))


#Создаём пустой словарь freq.
#Проходим по каждому символу char в строке s.
#Используем get(char, 0) + 1, чтобы увеличить счётчик символа.
#Возвращаем словарь с частотами.




4. Простые числа: Напишите функцию, которая возвращает список всех
простых чисел до заданного числа n.

#1
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(n):
    primes = [num for num in range(2, n) if is_prime(num)]
    return primes

# Пример использования
print(prime_numbers(20))


#Функция is_prime(num):

#Проверяет, является ли число num простым.
#Число простое, если оно больше 1 и не делится на другие числа (кроме 1 и себя).
#Для оптимизации проверка делителей проводится только до квадратного корня числа.
#Функция prime_numbers(n):

#Проходит по всем числам от 2 до n и добавляет в список primes те, которые являются простым



#2
count_primes = lambda x : len(reduce(lambda acc, y: list(filter(lambda z: (z==y) or (z % y != 0), acc)), [i for i in range(2, x+1)], [i for i in range(2, x+1)]))

4. Простые числа
python
Копировать код
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(n):
    primes = [num for num in range(2, n) if is_prime(num)]
    return primes

# Пример
print(prime_numbers(20))
Пояснение:
Проверяем простое ли число с помощью деления до квадратного корня. Строим список всех простых чисел до n.

5. Факториал
# Рекурсия
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

# Итерация
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Пример
print(factorial_recursive(5))  # 120
print(factorial_iterative(5))  # 120
Пояснение:
Факториал — это произведение всех чисел от 1 до n. Можно вычислить как рекурсивно, так и итеративно.

6. Палиндром

def is_palindrome(s):
    return s == s[::-1]

# Пример
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
Пояснение:
Палиндром — это строка, которая читается одинаково слева направо и справа налево. Проверяем с помощью среза строки.

7. Удаление дубликатов
python
Копировать код
def remove_duplicates(lst):
    return list(set(lst))

# Пример
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
Пояснение:
Используем set, чтобы удалить дубликаты, и затем снова превращаем его в список.

8. Поиск максимального подмассива (Алгоритм Кадане)

def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Пример
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
Пояснение:
Алгоритм Кадане находит максимальную сумму подмассива с помощью динамического программирования.

9. Поиск второго максимума
python
Копировать код
def second_largest(lst):
    unique_lst = list(set(lst))  # Убираем дубликаты
    unique_lst.sort()
    return unique_lst[-2] if len(unique_lst) > 1 else None

# Пример
print(second_largest([10, 20, 4, 45, 99]))  # 45
Пояснение:
Сначала убираем дубликаты, сортируем список и возвращаем предпоследний элемент.

10. Ротация списка
python
Копировать код
def rotate_list(lst, k):
    k = k % len(lst)  # На случай, если k больше длины списка
    return lst[-k:] + lst[:-k]

# Пример
print(rotate_list([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
Пояснение:
Ротация списка — это циклический сдвиг элементов на k позиций.

11. Функция-замыкание
python
Копировать код
def step_sequence(n):
    def generator(start=0):
        while True:
            yield start
            start += n
    return generator

# Пример
seq = step_sequence(3)
gen = seq()
print(next(gen))  # 0
print(next(gen))  # 3
Пояснение:
Замыкание возвращает генератор, который создаёт последовательность с шагом n.

12. Генерация бесконечной последовательности
python
Копировать код
def arithmetic_progression(start, step):
    while True:
        yield start
        start += step

# Пример
gen = arithmetic_progression(1, 2)
for _ in range(5):
    print(next(gen))
Пояснение:
Используем yield для создания бесконечной последовательности.

13. Функция с переменным количеством аргументов
python
Копировать код
def sum_args(*args):
    return sum(args)

# Пример
print(sum_args(1, 2, 3, 4, 5))  # 15
Пояснение:
*args позволяет принимать произвольное количество аргументов, которые можно сложить.

14. Фильтрация списка
python
Копировать код
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
Пояснение:
Используем filter для того, чтобы оставить только чётные числа.

15. Кастомный range
python
Копировать код
def my_range(start, stop, step=1):
    while start < stop:
        yield start
        start += step

# Пример
for i in my_range(1, 10, 2):
    print(i)
Пояснение:
Используем yield, чтобы создать свою версию функции range.

16. Класс “Круг”
python
Копировать код
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

# Пример
circle = Circle(5)
print(circle.area())  # 78.53981633974483
print(circle.circumference())  # 31.41592653589793
Пояснение:
Создаём класс Circle с методами для вычисления площади и длины окружности.

17. Класс “Автомобиль”
python
Копировать код
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        return f"{self.brand} {self.model} ({self.year})"

# Пример
car = Car("Toyota", "Corolla", 2020)
print(car.car_info())  # Toyota Corolla (2020)
Пояснение:
Класс Car с атрибутами и методом для вывода информации.

18. Класс “Стек”
python
Копировать код
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

# Пример
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # 2
print(stack.peek())  # 1
Пояснение:
Реализуем класс Stack с методами для работы со стеком.

19. Наследование
python
Копировать код
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Пример
dog = Dog()
cat = Cat()
print(dog.speak())  # Woof!
print(cat.speak())  # Meow!
Пояснение:
Переопределяем метод speak в классах-наследниках.

20. Множественное наследование
python
Копировать код
class A:
    def speak(self):
        return "A speaks"

class B:
    def speak(self):
        return "B speaks"

class C(A, B):
    pass

# Пример
c = C()
print(c.speak())  # A speaks
Пояснение:
Множественное наследование вызывает метод первого класса в MRO (метод разрешения порядка).

21. Чтение и запись в файл
python
Копировать код
# Чтение
with open("file.txt", "r") as file:
    lines = file.readlines()

# Сортировка
lines.sort()

# Запись обратно
with open("file.txt", "w") as file:
    file.writelines(lines)
Пояснение:
Читаем строки из файла, сортируем их и записываем обратно.

22. JSON
python
Копировать код
import json

# Сериализация
data = [1, 2, 3, 4, 5]
json_data = json.dumps(data)

# Десериализация
data_back = json.loads(json_data)
print(data_back)
Пояснение:
Используем json для сериализации и десериализации данных.

23. Логирование
python
Копировать код
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

# Логируем действия
logging.info("Программа запущена")
logging.info("Программа завершена")
Пояснение:
Используем модуль logging для записи логов в файл.

24. Алгоритм сортировки пузырьком
python
Копировать код
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Пример
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
Пояснение:
Сортировка пузырьком — это алгоритм, который многократно проходит по списку и меняет местами элементы, если они в неправильном порядке.

25. Двоичный поиск
python
Копировать код
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Пример
print(binary_search([1, 2, 3, 4, 5, 6], 4))  # 3
Пояснение:
Двоичный поиск позволяет найти элемент в отсортированном списке, деля его пополам на каждом шаге.

Челлендж: Угадай число
python
Копировать код
import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Угадай число от 1 до 100: "))
        attempts += 1
        if guess < number:
            print("Слишком мало!")
        elif guess > number:
            print("Слишком много!")
        else:
            print(f"Поздравляю! Ты угадал число за {attempts} попыток.")
            break

guess_number()
Пояснение:
Программа генерирует случайное число, и пользователь должен угадать его. Программа подсказывает, больше или меньше введённое число.

'''





