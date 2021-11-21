from dt import dzien

#print(dzien(1998,2,10))
for r in range (2021,2030):
    for m in range (1,13):
        if dzien(r,m,13) == 5:
            print(r,m,13)
