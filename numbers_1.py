from num2words import num2words

n = int(input("Введите любое число:"))

if n < 1 or n > 100000:
    print("Вы ввели неправильное число!")
    n = int(input("Введите число от 1 до 100000:"))

p = num2words(n, lang='ru')

if n % 10 == 1 and n != 11:
    rub = "рубль"
elif n % 10 in [2, 3, 4] and (n % 100 < 10 or n % 100 > 20):
    rub = "рубля"
else:
    rub = "рублей"

print(p, rub)
