import numpy as np
from numpy.linalg import LinAlgError

def wczytaj_dane(plik):
    odczyt=open(plik,'r')
    dane=odczyt.readlines()
    for x in range(len(dane)):
        dane[x]=dane[x].strip().split(" ")

    #end for
    #dane[0]=int(dane[0][0])
    for i in dane:
        i = list(map(int,i))
    #end for
    for x in range(len(dane)):
        #dane[x] = [int(i) for i in dane[x]]
        dane[x]=list(map(int,dane[x]))
    return dane
#end def
dane = (wczytaj_dane('dane.txt'))
stopien_rown = dane[0][0]
wspolczynnikiA= [x[:-1] for x in dane ]
wspolczynnikiA = wspolczynnikiA[1:]
wspolczynnikiB = [x[-1] for x in dane]
wspolczynnikiB = [wspolczynnikiB[1:]]
wspolczynnikiB = wspolczynnikiB[0]
ArrayA=np.array(wspolczynnikiA)
ArrayB=np.array(wspolczynnikiB)
try:
    rozw=np.linalg.solve(ArrayA,ArrayB)
except LinAlgError:
    print('układ nieoznaczony osobliwy lub niepoprawne dane')
except Exception as X:
    print("wystąpił inny błąd",X)
else:
    print("rozwiązanie:\n",rozw)
finally:
    print("Macierz A:\n",ArrayA)
    print("Macierz B:\n",ArrayB)