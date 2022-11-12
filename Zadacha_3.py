num = input('Введите вещественное число: ')
sum = sum(map(int, num.replace('.', '')))
print(f"Сумма цифр = {sum}")