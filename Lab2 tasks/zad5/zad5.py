def szyfruj(plik):
    try:
        tekst=open(plik,"r")
    except Exception as e:
        print("wystapil blad: \n",e)
    else:
        szyfr=[3,1,2,0,6]
        poz=0
        dane=tekst.readlines()
        for x in range(len(dane)):
            dane[x]=list(dane[x])
        #end for
        for x in range(len(dane)):
            for i in range(len(dane[x])):
                if (ord(dane[x][i]) >= 65) and (ord(dane[x][i])<=90):
                    dane[x][i]=chr(ord(dane[x][i])+szyfr[poz])
                    if ord(dane[x][i]) > 90:
                        dane[x][i]=chr(ord(dane[x][i])-26)
                    #end if
                    poz+=1
                    if poz == (len(szyfr)-1):
                        poz=0
                    #end if
                elif (ord(dane[x][i]) >= 97) and (ord(dane[x][i])<=122):
                    dane[x][i]=chr(ord(dane[x][i])+szyfr[poz])
                    if ord(dane[x][i]) > 122:
                        dane[x][i]=chr(ord(dane[x][i])-26)
                    #end if
                    poz+=1
                    if poz == (len(szyfr)-1):
                        poz=0
                    #end if
                #end if
            #end for
        #end for
        for x in range(len(dane)):
            dane[x] ="".join(dane[x])
        #end for
    return dane
#end def

def deszyfruj(plik):
    try:
        tekst=open(plik,"r")
    except Exception as e:
        print("wystapil blad: \n",e)
    else:
        szyfr=[3,1,2,0,6]
        poz=0
        dane=tekst.readlines()
        for x in range(len(dane)):
            dane[x]=list(dane[x])
        #end for
        for x in range(len(dane)):
            for i in range(len(dane[x])):
                if (ord(dane[x][i]) >= 65) and (ord(dane[x][i])<=90):
                    dane[x][i]=chr(ord(dane[x][i])-szyfr[poz])
                    if ord(dane[x][i]) < 65:
                        dane[x][i]=chr(ord(dane[x][i])+26)
                    #end if
                    poz+=1
                    if poz == (len(szyfr)-1):
                        poz=0
                    #end if
                elif (ord(dane[x][i]) >= 97) and (ord(dane[x][i])<=122):
                    dane[x][i]=chr(ord(dane[x][i])-szyfr[poz])
                    if ord(dane[x][i]) < 97:
                        dane[x][i]=chr(ord(dane[x][i])+26)
                    #end if
                    poz+=1
                    if poz == (len(szyfr)-1):
                        poz=0
                    #end if
                #end if
            #end for
        #end for
        for x in range(len(dane)):
            dane[x] ="".join(dane[x])
        #end for
    return dane
#end def
sz=szyfruj("tekst.txt")
zapis=open('tekst_zaszyfrowany.txt','w')
zapis.writelines(sz)
zapis.close()

print(sz)

desz=deszyfruj('tekst_zaszyfrowany.txt')
print(desz)