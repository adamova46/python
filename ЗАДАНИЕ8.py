my_dict = {1: '0101101', 2: '101110', 3: '1A14C', 4: '1100100', 5: '101010'}
print(my_dict)
my_dict.pop(3)  
print(my_dict)
my_dict[10] = '0100101'
print(my_dict)


sl = {'</>': 13, 'script': 1, '_init_': 10, 'self': 5, 'number_9': 6, '#comment': 100}
print(sl)
key = input('key: ')  
value = input('value: ')  
sl[key] = value
print(sl)

my_dict = {}

while len(my_dict) < 3:
    key = input("Введите ключ: ")
    if not key.isdigit():
        print("Ошибка! Ключ должен быть числом. Попробуйте ещё раз.")
        continue 
    key = int(key)  
    value = input("Введите значение: ")
    my_dict[key] = value
    print(f"Текущий словарь: {my_dict}")
print("Финальный словарь:", my_dict)



all_d = {1: 15, 4: 80, 44: 0, 256: 15, 100: 70, 101: 70, 20: 44, 3: 9}
all_d.pop(1)
all_d.pop(101)
all_d.pop(3)
print(all_d)


