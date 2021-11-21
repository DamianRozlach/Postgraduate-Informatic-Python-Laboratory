from random import randint

x=randint(1,100)
y=0
a=1
b=100

while x!=y:
    #y=int(input('Podaj liczbe'))
    y= (a+b)//2
    if y<x:
        print('za malo',y)
        a=y
    elif y>x:
        print('za duzo',y)
        b=y
#end while
print('Dobrze',y)
