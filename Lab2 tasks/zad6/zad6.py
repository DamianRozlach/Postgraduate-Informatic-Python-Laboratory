import matplotlib.pyplot as plt
import numpy as np
funkcja=input("podaj wzor funkcji f(x)=\n")
dol=int(input("podaj dolną granice przedzialu:\n"))
gora=int(input("podaj górną granice przedziału:\n"))

x=np.linspace(dol,gora,100)
y=[eval(funkcja) for x in x]

plt.plot(x,y)
plt.show()
pass


