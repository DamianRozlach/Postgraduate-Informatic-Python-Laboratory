def waga1(lista,n):
  s = 0
  for i in range(len(lista)-1,-1,-1):
    if s+lista[i]<=n:
      s += lista[i]
    if s==n:
      return True
  # end for
  return False
# end def


def waga(lista,n,p=0):
    if n==0: return True
    if p==len(lista): return False
    return waga(lista,n-lista[p],p+1) or waga(lista,n,p+1) or waga(lista,n+lista[p],p+1)
# end def

odw = [1,3,9,27]

for x in range(1,41):
  print(x,waga(odw,x))

print("ok")