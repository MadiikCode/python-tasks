# class Person:
#     name = None
#     age = None
#
# P = Person
# P.name = 'Madi'
# P.age = 15
# Person.__dict__
# print(Person.__dict__)


# class Person:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         print(f"Имя:{self.name},Возраст:{self.age} ")
#
# class Marlen(Person):
#     def __init__(self, name,age, hobby):
#         self.name = name
#         self.age = age
#         self.hobby = hobby
#
#     def __str__(self):
#         print(f"Имя:{self.name},Возраст:{self.age}, Хоби:{self.hobby}")
#
#
#
# class Ailarkyn(Marlen):
#     def __init__(self, name, age,hobby, job):
#         super().__init__(name,age,hobby)
#         self.job = job
#
#     def __str__(self):
#         print(f"Имя:{self.name}, Возраст:{self.age}, Хоби:{self.hobby}, Работа:{self.job}")
#
# A = Ailarkyn('Айжаркын',38,'reding', 'teacher')
# A.__str__()
#

'''
#1
class BankAccount:
    def __init__(self, owner,balance):
        balance1 = 0
        self.owner = owner
        self.balance = balance
        self.balance1 = balance1

    def deposit(self,amount):
        self.balance1 += amount
        print(f' Баланс пополнен на {amount}')

    def withdraw(self,amount):
        if amount > self.balance1:
            print(f'недостаточно средств')
        elif amount < self.balance1:
            self.balance1 = self.balance1 - amount
            print(f'Снято {amount}')

    def get_balance(self):
        return self.balance1

a = BankAccount('akhunbaeva',2000)
a.deposit(1500)
a.withdraw(100)
print(a.get_balance())




#2
class Book:
    def __init__(self, title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        print(f'{self.title}, {self.author}, {self.year}')

class Library(Book):
    def __init__(self, title,author,year):
        super().__init__(title, author,year)
        self.a = []

    def __str__(self):
        super().__str__()

    def add_book(self, book):
        self.a.append(book)
        print(f'Китеп кошулду:{book.title}')

    def remove_book(self,title):
        for i in self.a:
            if i.title == title:
                self.a.remove(i)
                print('Китеп очурулду')
                return
        print('Китеп табылбады')

    def find_book(self,title):
        self.title = title
        for book in self.a:
            if book.title == title:
                return book
        print('Сиз издеп жаткан китеп жок')




book1 = Book('Кто я?','',2222)
book2 = Book('','',2000)

L = Library('','',1933)
L.add_book(book1)
L.add_book(book2)
L.find_book('')




#5
class Animal:
    def ggg(self):
        return ''

class Cat(Animal):
    def ggg(self):
        return 'Мяу'

class Dog(Animal):
    def ggg(self):
        return 'Вофф'

cat1 = Cat()
dog2= Dog()

print(cat1.ggg())
print(dog2.ggg())


#чат gpt
#1
class Vehicle:
    def __init__(self,speed):
        self.speed = speed

    def move(self):
        return f"Moving at {self.speed} km/h"
    def __str__(self):
        return self.move()


class Car(Vehicle):
    def __init__(self):
        super().__init__(100)
        print('Ваша скрость 100km/h ')

class Bike(Vehicle):
    def __init__(self):
        super().__init__(20)
        print('Ваша скорость 20 km/h')



car = Car()
bike = Bike()

print(car)
print(bike)



#2
class Employee:
    def __init__(self,name):
        self.name = name

    def work(self):
        return 'Working'

class Manager(Employee):
    def __init__(self):
        super().__init__('Adrey')

    def work(self):
        return f"{self.name} is managing the team"
class Developer(Employee):
    def __init__(self):
        super().__init__('Job')

    def work(self):
        return f"{self.name} is writing code"

m = Manager()
p = Developer()

print(p.work())
print(m.work())


#4
class Account:
    def __init__(self, owner,balance):
        self.owner = owner
        self.balance = balance

    def info(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"

class SavingsAccount(Account):
    def add_interest(self):
        self.balance *= 1.05


class _account(Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Вы сняли {amount}. Новый баланс: {self.balance}")
        else:
            print("Недостаточно средств на счёте")


# Примеры использования
a = Account('Akhunbaeva', 100)
print(a.info())  # Owner: Akhunbaeva, Balance: 100

s = SavingsAccount('Akhunbaeva', 1000)
s.add_interest()
print(s.info())  # Owner: Akhunbaeva, Balance: 1050.0

c = _account('Akhunbaeva', 500)
c.withdraw(100)
print(c.info())  # Owner: Akhunbaeva, Balance: 400

'''


import math
import sqlite3
'''
# class Person:
#     def __init__(self,name,age,job):
#         self.name = name
#         self.age = age
#         self.job = job
#
#     def info(self):
#         print(f'Имя: {self.name}, Возраст: {self.age}, Работа: {self.job}')
#
# class Aijan(Person):
#     def init(self,name,age,job, married):
#         super().init(name,age,job)
#         self.married = married
#
#     def info(self):
#         self.married = 'Замужем' if self.married == True else 'Не замужем'
#         info_about_aijan = super().info()
#         print(info_about_aijan, 'Замужем ли:', self.married)
#
# aijan = Aijan('Aijan',26,'Teacher', True)
# aijan.info()
#
#
# class Muslima(Person):
#     def init(self,name,age,job):
#         super().init(name,age,job)
#
#     def info(self):
#         info_about_muslima = super().info()
#         print(info_about_muslima)
#
# muslima = Muslima('Muslima',16,'Student')
# muslima.info()
#---#


class Car:
    model = ''
    mark = ''
    color = ''
    speed = 0
    year = 0

    def drive(self):
        if self.speed > 180:
            return 'Быстро ездит'
        elif self.speed > 250:
            return 'Ездит очень быстро'
        elif self.speed < 150:
            return 'Ездит медленно'

    def whom(self):
        if self.color == 'Red':
            return 'Для женщин'
        else:
            return 'Для мужнин'

    def method_year(self):
        if self.year < 2000:
            return 'Очень старая машина'
        else:
            return 'Достаточно навая'


class Kia(Car):
    tubina = True

    def drive(self):
        return super().drive()


    def whom(self):
        super().whom()
        if self.color == 'Red':
            return 'Для женшин и так же для мужшин'
        return 'Для женшин и так же для мужшин'

car1 = Car()

car1.color = 'Red'

kia1 = Kia()
kia1.model = 'Kia'
kia1.mark = 'Carnival'
kia1.color = 'Red'
kia1.speed = 43
kia1.year = 2112

print(car1.whom())
print(kia1.whom())

#класс животные

class Animals:
    def __init__(self, name , age ,  location_in_life):
        self.name = name
        self.age = age
        self.location_in_life = location_in_life

    def __str__(self):
        return f" Имя: {self.name}, Возраст: {self.age} , Место обитания : {self.location_in_life} "


class Cat(Animals):
    def __init__(self,name,age,location,meow):
      super().__init__(name,age,location)


    def __str__(self):
        info = super(Animals , self).__str__()
        return f"{info}"

cat = Cat('Shuni', 1,'Japan', '')
print(cat.__str__())






class Person:
    def __init__(self, name , age , job):
        self.name = name
        self.age = age
        self.job = job

    def info(self):
        print(f" Имя:{self.name}, Возраст: {self.age}, Робота: {self.job} " )


class Madina(Person):
    def __init__(self , name,age,job):
        super().__init__(name,age,job)

    def info(self):
        info_about_madi = super().info()
        print(info_about_madi)

madi = Madina('Madina',15,'')
madi.info()
'''





'''
class Person:
    def init(self,name,age,job):
        self.name = name
        self.age = age
        self.job = job

    def info(self):
        print(f'Имя: {self.name}, Возраст: {self.age}, Работа: {self.job}')

class Aijan(Person):
    def init(self,name,age,job, married):
        super().init(name,age,job)
        self.married = married

    def info(self):
        self.married = 'Замужем' if self.married == True else 'Не замужем'
        info_about_aijan = super().info()
        print(info_about_aijan, 'Замужем ли:', self.married)

aijan = Aijan('Aijan',26,'Teacher', True)
aijan.info()


class Muslima(Person):
    def init(self,name,age,job):
        super().init(name,age,job)

    def info(self):
        info_about_muslima = super().info()
        print(info_about_muslima)

muslima = Muslima('Muslima',16,'Student')
muslima.info()
'''

# class Person:
#     def init(self,name,age,job):
#         self.name = name
#         self.age = age
#         self.job = job
#
#     def info(self):
#         print(f'Имя: {self.name}, Возраст: {self.age}, Работа: {self.job}')
#
# class Aijan(Person):
#     def init(self,name,age,job, married):
#         super().init(name,age,job)
#         self.married = married
#
#     def info(self):
#         self.married = 'Замужем' if self.married == True else 'Не замужем'
#         info_about_aijan = super().info()
#         print(info_about_aijan, 'Замужем ли:', self.married)
#
# aijan = Aijan('Aijan',26,'Teacher', True)
# aijan.info()
#
#
# class Muslima(Person):
#     def init(self,name,age,job):
#         super().init(name,age,job)
#
#     def info(self):
#         info_about_muslima = super().info()
#         print(info_about_muslima)
#
# muslima = Muslima('Muslima',16,'Student')
# muslima.info()
#---#

'''

class Car:
    model = ''
    mark = ''
    color = ''
    speed = 0
    year = 0

    def drive(self):
        if self.speed > 180:
            return 'Быстро ездит'
        elif self.speed > 250:
            return 'Ездит очень быстро'
        elif self.speed < 150:
            return 'Ездит медленно'

    def whom(self):
        if self.color == 'Red':
            return 'Для женщин'
        else:
            return 'Для мужнин'

    def method_year(self):
        if self.year < 2000:
            return 'Очень старая машина'
        else:
            return 'Достаточно навая'


class Kia(Car):
    tubina = True

    def drive(self):
        return super().drive()


    def whom(self):
        super().whom()
        if self.color == 'Red':
            return 'Для женшин и так же для мужшин'
        return 'Для женшин и так же для мужшин'

car1 = Car()

car1.color = 'Red'

kia1 = Kia()
kia1.model = 'Kia'
kia1.mark = 'Carnival'
kia1.color = 'Red'
kia1.speed = 43
kia1.year = 2112

print(car1.whom())
print(kia1.whom())



class Person:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def get_balance(self):
        return self.__balance

    @get_balance.setter
    def get_balance(self, new_balance):
        if not isinstance(self.__balance, int):
            raise ValueError('Не правильный ввод баланса')
        self.__balance = new_balance
p = Person('Name', 5)
p.get_balance = 5
print(p.get_balance)


Написать класс который, имеет поле array
и реализует инкапсуляцию по отношению array,
так чтобы она не оставалось пустым
и не присваивалось туда дублирующиеся значения

Написать набор классов,
которые реализуют методы:
 - get() - получает последний элемент из массива - array
 - update() - обновляет последний элемент из массива - array
 - pop() - удаляет последний элемент из массива - array



class WorkWithArray:
    def __init__(self, array):
        self._array = array

    @property
    def get_array(self):
        return self._array

    @get_array.setter
    def get_array(self, value):
        if not self._array:
            raise ValueError('Поле не должно оставаться пустым.')
        if len(self._array) != len(set(self._array)):
            raise ValueError('Поле не должно дублироваться.')

        self._array[-1] = value





class GetArray(WorkWithArray):
    def __init__(self, _array):
        super().__init__(_array)

    def get(self):
        return self._array[-1]


#res = GetArray([1, 2, 3])
#print(res.get())


class UpdateArray(WorkWithArray):
    def __init__(self, _array):
        super().__init__(_array)

    def update(self,value):
        if value in self._array:
            raise ValueError("Дубликаты не допускаются")
        self._array[-1] = value
        return self._array



class DeleteArray(WorkWithArray):
    def __init__(self, _array):
        super().__init__(_array)

    def pop(self):
        if not self._array:
            raise ValueError("Нечего удалять — массив пуст")
        self._array.pop()



res = GetArray([1, 2, 3])
print(res.get())

res2 = DeleteArray([0,9,8])
res2.pop()
print(res2.get_array)

res3 = UpdateArray([7,7,7])
print(res3.update(5))


def decorator_wrapper(arg1, arg2):
    def my_decor(func):
        def wrapper(*args, **kwargs):
            print('Before:', arg1, arg2)
            result = func(*args, **kwargs)
            print('After')
            return result
        return wrapper
    return my_decor


@decorator_wrapper("Первый аргумент", "Второй аргумент")
def prn_hello():
    print('Hello')

prn_hello()

'''
'''
#задачи 
class Dog:
    def __init__(self, name, old ):
        self.name = name
        self.old = old

    def bark(self):
        return 'гав '


dog = Dog('Bob',2)
print(dog.bark())


#2
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def calculate_the_area_of_the_circle(self):
        area = math.pi * (self.radius ** 2)
        return area

circle = Circle(60)
print(circle.calculate_the_area_of_the_circle())



#3
class Book:
    def __init__(self,name,author):
        self.name = name
        self.author = author

    def information(self):
        return f"Название книги:{self.name} Автор: {self.author}"


bookk = Book('Охо́та на ове́ц','Мураками')
print(bookk.information())


#4
class Car:
    def __init__(self,stamp, year_of_release):
        self.stamp = stamp
        self.year_of_release = year_of_release


    def Start_the_car(self):
        return "Машина заведена"

car = Car('BMW M5 (F90) ', '2020')
print(car.Start_the_car())




#5
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def perimeter_calculation(self):
        P = 2 * (self.height + self.width)
        return P


rec = Rectangle(20,10)
print(rec.perimeter_calculation())

'''


