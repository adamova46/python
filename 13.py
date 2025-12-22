def alpha(user_string):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    user_chars = set(user_string.lower())
    used_chars = []
    for char in user_string.lower():
        if char in alphabet and char not in used_chars:
            used_chars.append(char)
    print(' '.join(used_chars))
    remaining_alphabet = []
    for char in alphabet:
        if char not in user_chars:
            remaining_alphabet.append(char)
    chunk_size = 5  
    for i in range(0, len(remaining_alphabet), chunk_size):
        chunk = remaining_alphabet[i:i + chunk_size]
        print(' '.join(chunk))
alpha('пайтон')




def create_calendar(month_name, year, days_count):
    print(f'calendar: {month_name} {year}')
    print()  
    day = 1  
    while day <= days_count:
        week = []  
        for _ in range(7):
            if day <= days_count:
                week.append(str(day))  
                day += 1  
            else:
                break  
        print(' '.join(week))
create_calendar('Randomner', 2045, 23)



def bin_sys(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        print(bin(num)[2:])
        total_sum += num
    print(f"сумма: {bin(total_sum)[2:]}")
bin_sys(3, 6)




def begin(field, row, col):
    field[row][col] = '*'
    return field  
field = [['[ ]', '[ ]', '[ ]'],
         ['[ ]', '[ ]', '[ ]'],
         ['[ ]', '[ ]', '[ ]']]
result = begin(field, 1, 2)
for row in result:
    print(row)



