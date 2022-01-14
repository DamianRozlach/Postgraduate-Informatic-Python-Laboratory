try:
    f = open('pan_tadeusz.txt','r',encoding='utf8')
except Exception as e:
    print("Nie udalo sie wczytac pliku,wystąpił błąd:",e)
else:
    ilosc={}
    dane = f.readlines()
    for x in dane:
        x=x.strip().split(" ")
        if len(x)>0:
            for i in x:
                if len(i)>4:
                    if i in ilosc:
                        ilosc[i]+=1
                    else:
                        ilosc[i]=1
                    #end if
                #end if
            #end for
        #end if
    #end for
    sorted_ilosc=sorted(ilosc.items(),key=lambda x: x[1])
    print("20 najczestrzych slow w teksie:",sorted_ilosc[-1:-20:-1],sep="\n")
#end try


