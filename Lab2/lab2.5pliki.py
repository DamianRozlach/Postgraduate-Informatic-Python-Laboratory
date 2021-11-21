try:
  t={} 
  f=open("tekst.txt","r",encoding="utf-8")
  for line in f:
      line=line.strip('\n').lower().split()
      #print(line)
      for z in line:
          t.setdefault(z,0)#stwarza t[z]=0 jesli nie istnieje z 
          t[z]=t[z]+1
  # end
  f.close()
except:
  print("brak pliku!")
# end
#for k in t:
 #   print(k,t[k])
l=t.items()
l2=sorted(l,key=lambda x:len(x[0]),reverse = True)
for k,w in l2:
  print(k,w)