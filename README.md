from random import randint   "Імпорт функціїї випадкових цілих чисел"

N=30   "Кількість випадкових чисел"

array=list()

for i in range (N):

    array.append (randint(-100, 100))   "Діапазон для випадкових чисел"

print("Список", array)

mx = 0   "Прирівнюємо максисмальне число до нуля"

for i in array:

    if i > mx:

        mx = i   "Перебір усіх чисел послідовно, для знаходження найбільшого"

print("Максимальний елемент", mx)


array.index(mx)    "Пошук индексу максимального числа"

print("Порядковий номер елементу", array.index(mx))

for j in array:

    divid = j %2

    if divid == 0:

        array.remove(j)   "Видалення зі списку парних чисел"

        array.sort(reverse = True)   "Реверсивне сортування списку(за спадання)"

print(array)
