'''
Для двух строк s и t мы говорим, что «t делит s» тогда и только тогда,
когда s = t + t + t + ... + t + t (то есть t повторяется один или несколько раз).
Даны две строки str1 и str2, верните самую длинную строку,xкотораяxделит обеstr1строки.str2

#1
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]

# Пример использования
solution = Solution()
str1 = "ABABAB"
str2 = "ABAB"
print(solution.gcdOfStrings(str1, str2))  # Вывод: "AB"


#2
def gcd_of_strings(str1: str, str2: str) -> str:
    from math import gcd

    base_length = gcd(len(str1), len(str2))
    base_string = str1[:base_length]

    if str1 == base_string * (len(str1) // base_length) and str2 == base_string * (len(str2) // base_length):
        return base_string
    return ""


# Пример использования
str1 = "ABCABC"
str2 = "ABC"
print(gcd_of_strings(str1, str2))  # Вывод: "ABC"


1️⃣ Эгер str1 + str2 менен str2 + str1 бирдей болбосо, аларда жалпы бөлүүчү жок → "" (бош сап) кайтарабыз.
2️⃣ Эң чоң бөлүүчү саптын узундугун табыш үчүн gcd(len(str1), len(str2)) колдонобуз.
3️⃣ Ошол узундукка жараша str1 ичинен бөлүктү кесип алабыз.





#3
class Solition:
    def kidsWithCandies(self,candies:list[int],extraCandies:int) -> list[bool]:
        max_candies = max(candies)
        result = []

        for i in candies:
            if(i+extraCandies):


Возвращает строку слов в обратном порядке, объединенную одним пробелом.
Ввод: s = «небо голубое»
Вывод: «голубое небо»




class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

# Пример использования:
solution = Solution()
s = "  hello   world  "
print(solution.reverseWords(s))  # Вывод: "world hello"
'''