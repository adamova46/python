a=int(input())
b=0
c=0
b=a//60
c=a%60
print(b,c)



a=8
b=12
f=int(input())
if f>=a and f<=b:
    print("Это нормально")
elif f<a:
    print("Недосып")
elif f>b:
    print("Пересып")




a=int(input())
b=int(input())
c=int(input())
p=(a+b+c)/2
s= (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(s)




a=str(input())
if a=="Круг":
    b=int(input())
    s=3,14*b**2
    print(s)
elif a=="Квадрат":
    b=int(input())
    s=b**2
    print(s)
elif a=="Треугольник":
    b=int(input())
    h=int(input())
    s=(b+h)/2
    print(s)





a=int(input())
if a==1:
    print(a,"Программист")
elif a>1 and a<5:
    print(a,"Программиста")
elif a>=5:
    print(a,"Программистов")




a=int(input())
c=a%10
v=a%100//10
k=a%1000//100
m=c+v+k
b=a//100000
s=a//10000 %10
d=a//1000%10
n=b+s+d
if n==m:
    print("Счастливый")
else:
    print("Не счастливый")
