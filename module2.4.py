# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
# Задача "Всё не так уж просто"
print('\nЗадача "Всё не так уж просто"')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("\nИмеем список\n",numbers)
primes = []
not_primes = []
print('''
Создаём два списка 
Primes     - простые числа
Not primes - не простые числа\n''')

for i in numbers:
    if i == 1:
        continue
    is_prime = True
    for j in range(2, i):
        if i == 2:
            break
        if i % j == 0 :
            is_prime = False
            break
    if  is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('\nPrimes: ', primes)
print('Not Primes: ', not_primes)
print("\nСписок проверен")
# Задание выполнено