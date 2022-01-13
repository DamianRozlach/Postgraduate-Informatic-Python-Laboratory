import numpy as np
from timeit import default_timer as timer
n = 0
n=int(input("podaj gorna granice zakresu: \n"))

def sito_lista(n):
    lista=[x for x in range(2,n)]
    pozycja=0
    while pozycja != (len(lista)-1):
        for x in lista:
            if x == lista[pozycja]:
                pass
            elif not x % lista[pozycja]:
                lista.remove(x)
            #end if
        #end for
        pozycja+=1
    #end while
    return lista
#end def

def sito_array(n):
    macierz = np.arange(2,n)
    pozycja = 0
    while pozycja != len(macierz):
        macierz=np.delete(macierz,np.argwhere((macierz % macierz[pozycja] == 0) & (macierz != macierz[pozycja])))
        pozycja += 1
    #end while
    return macierz
#end def

def sito_dict(n):
    slownik = {x:True for x in range(2,n)}
    for x in range(2,n):
        if slownik.get(x):
            for i in range((x+1),n):
                if not i % x:
                    slownik[i]=False
                #end if
            #end for
        #end if
    #end for
    wyniki=[x for x,y in slownik.items() if y]

    return wyniki
#end def 

start=timer()
print(sito_lista(n))
stop=timer()
print("czas wykonania z uzyciem listy: ",stop-start,"\n \n")

start=timer()
print(sito_array(n))
stop=timer()
print("czas wykonania z uzyciem macierzynumpy: ",stop-start,"\n \n")

start=timer()
print(sito_dict(n))
stop=timer()
print("czas wykonania z uzyciem słownika: ",stop-start,"\n \n")

                



