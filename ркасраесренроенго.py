m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m_1= []
k=0
r=[]
for row in m:
    for element in row:
        m_1.append(element)
        if element %2==0:
            k+=1
        else:
            r.append(element)
print(m_1)
print(r)
print(k)


matrix_1 = [[2, 4, 3, 6], [5, 7, 1, 5]]
matrix_2 = [[2, 9, 0, 2], [3, 4, 7, 6]]

answer_matrix = []
for i in range(len(matrix_1)):
    row = []
    for j in range(len(matrix_1[i])):
        row.append(0)
    answer_matrix.append(row)
for i in range(len(matrix_1)):
    for j in range(len(matrix_1[i])):
        answer_matrix[i][j] = matrix_1[i][j] * matrix_2[i][j]
print(answer_matrix)
for row in answer_matrix:
    row_sum = sum(row)
    print(f"{row} сумма строки: {row_sum}")



fruits = [['Banana', 'apple'], ['apricot', 'Avocado'], ['lime', 'lemon'], ['Mango', 'grapes']]
capitalized_fruits = []
for row in fruits:
    for fruit in row:
        if fruit and fruit[0].isupper():
            capitalized_fruits.append(fruit)
print("Элементы с заглавной буквы:", capitalized_fruits)




random_elements = [
    ['toy', 'bee', 'cheese', 'ear'],
    [False, 'word', '0110110', 10],
    ['happiness', '(J ^口^)J ', 'luck', None],
    ['car', '<- code ->', 4.7, True]
]
for row_index, row in enumerate(random_elements):
    for col_index, element in enumerate(row):
        if col_index % 2 == 0:
            print(f"Элемент с индексом {col_index} в строке {row_index}: {element}")



rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Введите значение элемента [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)
print("\nВаш двумерный массив:")
for row in matrix:
    print(row)
