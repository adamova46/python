def upper(t):
    result = ""  
    for char in t: 
        if char.isupper(): 
            result += char  
    if result:  
        print(result)  
    else:  
        pass 

upper('PriVet') 



def punct(txt):
    target_chars = {'!', '?', '.', ',', '('}
    count = 0
    for char in txt:
        if char in target_chars:
            count += 1
    return count
print(punct('(Как дела?)'))  



def create_cube(x, y):
    for i in range(y): 
        print('*' * x) 

create_cube(5, 3)



def double(text):
    result = '' 
    for char in text:  
        result += char * 2  
    return result 
print(double('строка')) 





def Constructor(details, figures, cars, trees):
    required_details = 72
    required_figures = 4
    required_cars = 2
    required_trees = 7
    possible_details = details // required_details
    possible_figures = figures // required_figures
    possible_cars = cars // required_cars
    possible_trees = trees // required_trees
    total_sets = min(possible_details, possible_figures, possible_cars, possible_trees)
    return total_sets
print(Constructor(144, 8, 4, 14))  
print(Constructor(10000, 16, 6, 2))  



def create_list(length, number=0):
    return [number] * length
print(create_list(5,3))  
print(create_list(3))     


def custom_filter(data_list):
    total_sum = 0
    for item in data_list:
        if isinstance(item, int):
            if item % 7 == 0:
                total_sum += item 
    print(f"сумма: {total_sum}")
    return total_sum <= 83
print(custom_filter([7, 10.5, 'txt', 14, 2, 56]))



def square(x, y):
    numbers_row = "| " + " | ".join(str(i) for i in range(1, x + 1)) + " |"
    underline_top = "  " + "  _  ".join([""] * x) + "  "
    underline_bottom = "  " + "  ^  ".join([""] * x) + "  "
    result = ""
    for i in range(y):
        result += underline_top + "\n"
        result += numbers_row + "\n"
        result += underline_bottom + "\n"
    print(result)
square(2, 3)
