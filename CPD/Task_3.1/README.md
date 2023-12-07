#ЗАДАНИЕ:

TCP Client-streaming (Клиент, например, раз в 1 секунду отправляет данные на сервер), используя встроенный в Python модуль socket.
Task_3_1_server.py Task_3_1_client.py Используя encode() и decode()

# РЕЗУЛЬТАТ РАБОТЫ:

![image](https://github.com/Triceratops228/Triceratops228-Timur_Gallyamov_20321_HMI_CPD/assets/146287277/cfa30b5c-538e-470c-aff3-c9a2ce57e5ff)

# ПОЯСНЕНИЕ:

Каждую секунду на сервер посылается время жизни процессора

# ЛИСТИНГ:

# КЛИЕНТСКАЯ ЧАСТЬ:

``` py
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
```

# CЕРВЕРНАЯ ЧАСТЬ:

``` py
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
```
