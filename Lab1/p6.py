from random import randint

for n in range (20,50):
    licz=0
    for j in range (1000):
        t=[0 for _ in range (366)]


        for i in range (n):
            dz=randint(1,365)
            t[dz]+=1
        ok = False
        for i in range (1,366):
            if t[i] > 1:
                ok = True

        if ok:
            licz+=1
    print(n,licz/10,'%')
