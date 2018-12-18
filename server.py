import socket, time

#host = socket.gethostbyname(socket.gethostname())
host = "0.0.0.0"
port = 8888

clients = []

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))

quit = False
print("[ Server Started ]")

while True:
	try:
		data, addr = s.recvfrom(1024)

		if addr not in clients:
			clients.append(addr)

		itsatime = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

		print("["+addr[0]+"]=["+str(addr[1])+"]=["+itsatime+"]/",end="")
		print(data.decode("utf-8"))

		for client in clients:			#если адрес клиента такой же как у отправляющего, то ему сообщение не показываецца
			if addr != client:
				s.sendto(data,client)
	except:
		print("\n[ Server Stopped ]")
		break

s.close()
