def a(number):
    if number<0:
        return -number
    elif number == 0:
        return 1
    else:
        return number
print(a(int(input())))



def a(strin):
    if "," in strin or "." in strin:
        return True
    else:
        return False
print(a(str(input())))


def a(number, number2):
    if number%3==0 and number2%3==0:
        return True
    elif number%3==0 or number2%3==0:
        return "Одно число делится на 3"
    else:
        return False
print(a(int(input()),int(input())))



def a(number):
    if number>100:
        return "*"
    elif number<0:
        return ""
    else:
        return number * "*"
print(a(int(input())))


def a(str1, str2):
    if str1 == str2:
        return True
    else:
        return False
print(a(str(input()),str(input())))


def a(r,g,b):
    if r==0 and g==0 and b==0:
        return "Черный цвет"
    elif r==255 and g==255 and b==255:
        return "Белый цвет"
    elif r==255 and g==0 and b==0:
        return "Красный цвет"
    elif r==0 and g==255 and b==0:
        return "Зеленый цвет"
    elif r==0 and g==0 and b==255:
        return "Синий цвет"
    else:
        return "Нет цвета"
print(a(int(input()),int(input()),int(input())))



def a(d):
    if d>0:
        return d-1, d, d+1
    else:
        return 1
print(a(int(input())))


def a(str1):
    if "doc" in str1:
        return "Word file"
    elif "txt" in str1:
        return "text file"
    elif "py" in str1:
        return "gfgf"
print(a(str(input())))



def stor(a,b,c):
    if a==b==c:
        return "Равносторонний треугольник"
    elif a!=b and a==c:
        return "Равнобедренный треугольник"
    elif a!=b!=c:
        return "Разносторонний треугольник"
    elif a+b>c or a+c>b or b+c>a:
       return "Разносторонний треугольник" 
    else:
        return "нет такого"
print(stor(int(input()), int(input()), int(input())))



text ="important information in one line"
def a(s):
    if s in text:
        return True
    else:
        return False
print(a(str(input())))


def a(s,d):
    if  s==d:
        return "Квадрат", s**2
    else:
        return "Прямоугольник", s*d
print(a(int(input()), int(input())))




print("Как твои дела")
def a(s):
    if s=="Хорошо" or s=="Нормально" or s=="Отлично":
        return "☺"
    elif s=="Плохо" or s=="Не хорошо":
        return ":("
    else:
        return ":|"
print(a(str(input())))
    



def a(s,d):
    if  s>d:
        return s**d
    elif s<d:
        return d**s
    else:
        return d +s
print(a(int(input())))



new_massage="Hello!How are you?"
def a(s):
    if s[0] == new_massage[0]:
        print(True)
    else:
        print(False)
print(a(int(input())))


def a(s,d):
    if s==d:
        print("Отрезки равны")
    elif s>d:
        print("Первый длиннее на", s-d)
    else:
        print("Второй длиннее на",d-s)
print(a(int(input()),int(input())))


def a(s):
    if s[0] == s[-1]:
        print(True)
    else:
        print(False)
print(a(int(input())))


def a(s):
    if s%2 == 0:
        print(s**2)
    elif s%3==0:
        print(s**3)
    else:
        print(s*100)
print(a(int(input())))


def a(s,d):
    if s<0 and d<0:
        print(False)
    elif s<0:
        print(s+1000,d)
    elif d<0:
        print(a,b+1000)
    else:
        print(s,d)
print(a(int(input()),int(input())))




def a(s):
    if s[-1] == "я" or s[-1] == "и" or s[-1] == "е" or s[-1] == "ю" :
        print(True)
    else:
        print(False)
print(a(int(input())))


def stor(a,b,c):
    if a<=0 or b<=0 or c<=0:
        print(False)
    else:
        print(True)
print(stor(int(input()), int(input()), int(input())))



def a(s):
    if s[-1]==0:
        print(s**10)
    elif s[-1]==1:
        print(s%3)
    elif s[-1]==2:
        print(s//2)
    else:
        print(s**2)
print(a(int(input())))


def a(s):
    if len(s)<8 or s=="qwerty123":
        print(False)
    else:
        print(True)
print(a(int(input())))


pc_number =777
def a(s,d):
    if s<pc_number<d or d<pc_number<s:
        print(True)
    else:
        print(False)
print(a(int(input()),int(input())))
