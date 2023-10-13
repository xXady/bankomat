from num2words import num2words

n = int(input("Введите любое число:"))

p = num2words(n, lang='ru')

if n % 10 == 1 and n != 11:
    rub = "рубль"
elif n % 10 in [2, 3, 4] and (n % 100 < 10 or n % 100 > 20):
    rub = "рубля"
else:
    rub = "рублей"

print(p, rub)