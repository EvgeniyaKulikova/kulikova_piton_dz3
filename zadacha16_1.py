#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input("Размер массива: ")) 
print("Элементы массива:")
lst = [int(input()) for i in range(n)]
print(lst)
x = int(input('Введите любое натуральное число '))
count = 0
for i in range(n):
    if lst [i] == x:
        count +=1
print(f'Заданное число {x} встречается в списке {count} раз')
