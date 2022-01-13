import numpy as np

def wczytaj_dane(plik):
    odczyt=open(plik,'r')
    dane=odczyt.readlines()
    for x in range(4):
        dane[x]=dane[x].strip().split(" ")

    #end for
    #dane[0]=int(dane[0][0])
    for i in dane:
        i = list(map(int,i))
    return dane
#end def

ArrayA=np.array(wczytaj_dane('dane.txt')[1:])
print(ArrayA)