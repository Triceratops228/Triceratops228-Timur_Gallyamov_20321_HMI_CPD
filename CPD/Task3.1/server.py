import socket
import time
 
server = socket.socket()            # создаем объект сокета сервера
hostname = socket.gethostname()     # получаем имя хоста локальной машины
port = 12345                        # устанавливаем порт сервера
server.bind((hostname, port))       # привязываем сокет сервера к хосту и порту
server.listen(5)                    # начинаем прослушиваение входящих подключений

print("Server starts")

 
con, addr = server.accept()     # принимаем клиента
print("connection: ", con)
print("client address: ", addr)

message = "Hello Client!"       # сообщение для отправки клиенту
con.send(message.encode())      # отправляем сообщение клиенту
con.close()                     # закрываем подключение

print("Server ends")
server.close()
