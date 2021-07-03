from random import randint
N=30
array=list()
for i in range (N):
    array.append (randint(-100, 100))
print("Список", array)

mx = 0
for i in array:
    if i > mx:
        mx = i
print("Максимальний елемент", mx)

array.index(mx)
print("Порядковий номер елементу", array.index(mx))

for j in array:
    divid = j %2
    if divid == 0:
        array.remove(j)
        array.sort(reverse = True)
print(array)
