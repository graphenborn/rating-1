from os import replace
import os
import sys
# Метод быстрой сортировки по возрастанию
def partition(unic, low, high):  
    pivot = unic[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while unic[i] < pivot:
            i += 1

        j -= 1
        while unic[j] > pivot:
            j -= 1

        if i >= j:
            return j

        unic[i], unic[j] = unic[j], unic[i]
        
def quick_sort(unic):  
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(unic, 0, len(unic) - 1)


#Метод пузырька по убыванию
def bubble_sort(unic):
    swapped = True
    while swapped:
        swapped = False
        for i in range (len(unic) - 1):
            if (unic[i] < unic[i+1]):
                unic[i], unic[i+1] = unic[i+1], unic[i]
                swapped = True

#Чтение Файлов
source = open('source_data.txt', encoding='utf-8')
res = open('result.txt', 'w', encoding='utf=8')
FIO = source.readline().strip()
ID = source.readline().strip()

# Запись в файл
res.write("1. Исходные данные: " + FIO + "; " + "ID: " + ID + "\n")

#Считаем число, на основе которого будет выбрано направление сортировки
num = int(int(ID) / len(FIO))

# Запись в файл
res.write("2. " + str(num) + "\n")

if (num % 2 == 0):
    direct = "по возрастанию"
    parity = "четное"
else:
    direct = "по убыванию"
    parity = "нечетное"

# Запись в файл
res.write("3. Направление сортировки: " + direct + ", так как число " + str(num) + " - " + parity + "\n")

#Перевод строки в ID юникода
unic = FIO.replace(" ", "")
unic = [ord(c) for c in unic]

# Запись в файл
res.write("4. Набор данных: " + str(unic) + "\n")

#Определяем направление сортировки и сортируем
if (num%2 == 0):
    quick_sort(unic)
 # Запись в файл   
    res.write("5. Отсортированный " + direct + " набор данных " + str(unic) + "\n")
else:
    bubble_sort(unic)
# Запись в файл
    res.write("5. Отсортированный " + direct + " набор данных " + str(unic) + "\n")

# Складываем элементы списка
sum = unic[0]
for i in range (1,len(unic)):
    sum += unic[i]

#Ищем среднее арифметическое
s_arif = round(sum / len(unic), 3)

# Запись в файл
res.write("6. Среднее арифметическое значение: " + str(s_arif) + "\n")

#Склаыдваем квадраты элементов списка
sum = unic[0]**2
for i in range (1,len(unic)):
    sum += unic[i]**2

#ищем среднее квадратическое
s_kvad = round((sum / len(unic))**0.5, 3)

# Запись в файл
res.write("7. Среднее квадратическое значение: " + str(s_kvad))

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def print_file(file_path):
    file_path = resource_path(file_path)
    with open(file_path) as fp:
        for line in fp:
            print(line)

if __name__ == '__main__':
    print_file('source_data.txt')
    print_file('result.txt')
