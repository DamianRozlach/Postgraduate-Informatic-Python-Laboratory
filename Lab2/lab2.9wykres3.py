import socket
import time

from pylab import *
import xmltodict

################################################################################
    
def get_meteo():
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect(('meteo2.ftj.agh.edu.pl',80))
  sock.send(b"GET /meteo/meteo.xml\n")
  s = sock.recv(1024).decode()
  sock.close()
  return s
# end def

################################################################################

l = []  
while True:
  t = get_meteo()
  print(t)

  d = xmltodict.parse(t)
  x = d['meteo']['dane_aktualne']['sx']
    
  print(x)

  v = float(x[:-4])

  l.append(v)
  print(l)
  plot(l)
  savefig("wykres.jpg")
  time.sleep(60)
# end while
