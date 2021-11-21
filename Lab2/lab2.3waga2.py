def waga(li,n,p,wynik):
    if n==0: print(wynik)
    if p==len(li): return 
    waga(li,n-li[p],p+1,wynik+[li[p]])
    waga(li,n+li[p],p+1,wynik+[-li[p]])
    waga(li,n,p+1,wynik)
# end def

odw = [1,3,5,10,16,24]
wyniki=[]
for x in range(1,41):
  print(x)
  waga(odw,x,0,wyniki)


print("ok")