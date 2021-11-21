n= int(input('podaj liczbe'))
licz=0
while n!=1:
    licz += 1
    if n%2 == 0:
        n=n/2
    else:
        n=3*n +1
    print(n)
print('koniec n=',n,'prob',licz)
