import socket
import file_pb2

server = socket.socket()            # создаем объект сокета сервера
hostname = ""    # получаем имя хоста локальной машины
port = 8080                        # устанавливаем порт сервера
server.bind((hostname, port))       # привязываем сокет сервера к хосту и порту
server.listen(5)                    # начинаем прослушиваение входящих подключений
msg = file_pb2.TempEvent()
print("Server running")
con, _ = server.accept() 
while True:    # принимаем клиента
    data = con.recv(1024)
    msg.ParseFromString(data)
    print(msg.message)
con.close()