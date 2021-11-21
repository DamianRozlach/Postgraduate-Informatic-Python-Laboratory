import socket
import xmltodict

#pip3 install xmltodict 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('meteo2.ftj.agh.edu.pl',80))
sock.send(b"GET /meteo/meteo.xml\n")
s = sock.recv(1024).decode()
sock.close()

print(s)
print()

doc = xmltodict.parse(s)
print(doc)

for x in doc['meteo']['dane_aktualne']:
    print(x,doc['meteo']['dane_aktualne'])
  