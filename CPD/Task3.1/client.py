import socket
import time
client = socket.socket()            # создаем сокет клиента
hostname = socket.gethostname()     # получаем хост сервера
port = 12345                        # устанавливаем порт сервера
client.connect((hostname, port))    # подключаемся к серверу
data = client.recv(1024)            # получаем данные с сервера
print("Server sent: ", data.decode('utf = 8'))    # выводим данные на консоль
while True:    
    time.sleep(1)
    print(time.time())
client.close()

