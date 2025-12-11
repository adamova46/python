m = [
    ['folder', 'coursework.doc', 'folder', 'pict.png', 'data.accdb'],
    ['icon.ico', 'script.js', 'index.html', 'style.css', 'prog.py'],
    ['my song.mp3', 'anapa-2003.jpg', 'cs 1.6.exe', 'folder','cheat.txt'],
    ['notes.txt', 'main.py', 'work.pdf', 'cartoon.mp4','array.py'],
    ['project.psd', 'cycle.py', 'folder', 'cycle.js', 'turtle.py']
]
for row in m:
    print(row)

for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == 'data.accdb':
            m[i][j] = 'data.sql'
for i in range(len(m)):
    m[i] = [item for item in m[i] if item != 'folder']
processed_data = []
for row in m:
    new_row = []
    for item in row:
        if item != 'folder':
            if item == 'data.accdb':
                new_row.append('data.sql')
            else:
                new_row.append(item)
    processed_data.append(new_row)
for row in processed_data:
    print(row)
py_files = []
for row in m:
    for item in row:
        if item.endswith('.py'):
            py_files.append(item)
print(py_files)

js_files = []
for row in m:
    for item in row:
        if item.endswith('.js'):
            js_files.append(item + 'new')
print(js_files)




word_numb = ["ноль", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
n = int(input("Введите число от 0 до 9: "))
if 0 <= n <= 9:
    for i in range(n + 1):
        print(word_numb[i])
else:
    print("Введите число <= 9")




bin_sy = ['1101111', '11011101', '11000111', '11011100', '11011110']
decimal_numbers = []
for binary_num in bin_sy:
    decimal_num = int(binary_num, 2)
    decimal_numbers.append(decimal_num)
    print(f"Двоичное число {binary_num} в десятичной системе: {decimal_num}")
max_number = max(decimal_numbers)
min_number = min(decimal_numbers)
print(f"\nМаксимальное число: {max_number}")
print(f"Минимальное число: {min_number}")




A = [
    [-446, 281, -80],
    [465, 432, -122],
    [13, 'error', 8]
]
print("Исходная матрица:")
for row in A:
    print(row)
for i, row in enumerate(A):
    for j, element in enumerate(row):
        if isinstance(element, str):
            A[i][j] = len(element)
            print(f"Элемент [{i}][{j}] был строкой '{element}', заменён на {len(element)}")
print("\nМатрица после замены:")
for row in A:
    print(row)
total_sum = 0
for row in A:
    for element in row:
        total_sum += element
print(f"\nСумма всех элементов матрицы: {total_sum}")





matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Матрица 3x3:")
for row in matrix:
    print(row)
diagonal_sum = matrix[0][2] + matrix[1][1] + matrix[2][0]
print(f"\nСумма чисел по диагонали справа налево: {diagonal_sum}")
print(f"Расчёт: {matrix[0][2]} + {matrix[1][1]} + {matrix[2][0]} = {diagonal_sum}")
