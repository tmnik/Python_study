#генерируем случайный список и находим медиану
import random             #для случайных чисел
import statistics         #для нахождения медианы

numbers = []
numbers_size = random.randint(10,15)

for _ in range(numbers_size):
    numbers.append(random.randint(10,20))

print("Список:"numbers)
numbers.sort()
print("Отсортированный:",numbers)

print("Длина списка:",len(numbers))

half_size = len(numbers)//2 #целочисленное деление
median = None
if numbers_size%2==1:
    median = half_size
else:
    median = sum(numbers[half_size-1:half_size+1])/2
print("Медиана расчет:",median)
print("Медиана:",statistics.median(numbers))
