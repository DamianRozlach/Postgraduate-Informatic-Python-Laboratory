def IsArmstrong(liczba):
    liczbastring=str(liczba)
    lista=[]
    for x in range(len(liczbastring)):
        lista.append(int(liczbastring[x]))
    #endfor
    suma = 0
    for x in lista:
        suma+=pow(x,3)
    #endfor
    return(suma == liczba)
#end def
Armstrong=set()
for x in range(1000000):
    if IsArmstrong(x):
        Armstrong.add(x)
    #end if
#end for

print(sorted(Armstrong))
