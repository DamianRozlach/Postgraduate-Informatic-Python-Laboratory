from math import sqrt

def sp(n):
    s=0
    for p in range(1,n):
        if n%p==0:
            s+=p
    return s
#end

def sp2(n):
    s=1
    p=2
    while p**2 < n:
        if n%p==0:
            s=s+p+n/p
        p = p+1
    if p**2 == n:
        s=s+p
    return s
#end

for a in range (1,1000000):
    if a == sp2(a):
      print(a,sp(a))
print("koniec")

    
