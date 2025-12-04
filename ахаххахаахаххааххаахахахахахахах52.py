m=["круг",0.25,"квадрат", "треугольник",15,"круг","овал","10"]
m2=["круг","квадрат","треугольник","овал"]
for item in m[:]:
    if item not in m2:
        m.remove(item)
print(m)


abs=['A','B','C','D','E','F','G']
n=len(abs)
a=abs[0]
b=abs[-2]
c=abs[-1]
del abs[:]
abs.append(a)
abs.append(b)
abs.append(c)
print(abs)


n=[1,4]
n.insert(1, 2)
n.insert(2, 3)
print(n)


m=[14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
m2=[num for num in m if num>=0]
m2.sort()
a=m2[:]
m2.sort(reverse=True)
a2=m2[:]
print(a)
print(a2)


a=[]
b=[]
c=[]
print("Введите количество чисел")
n=int(input())
for i in range(n):
    print("Введите число")
    x=int(input())
    if x>0:
        b.append(x)
    elif x==0:
        c.append(x)
    else:
        a.append(x)
s=sum(a)
if b:
    sr=sum(b)/len(b)
else:
    sr=0
stars=['*' if x==0 else x for x in c]
print(s)
print(sr)
print(len(stars),stars)
