"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""


s = int(input("Введите результат сложения двух чисел: "))
p = int(input("Введите результат произведения двух чисел: "))
flag = False
for x in range(s):
    for y in range(s):
        if x + y == s:
            if x * y == p:
                print(x, y)
                flag = True
                break
    if flag is True:
        break