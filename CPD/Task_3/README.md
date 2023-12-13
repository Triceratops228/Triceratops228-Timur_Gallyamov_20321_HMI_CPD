# ЗАДАНИЕ:

TCP Client-streaming (Клиент, например, раз в 1 секунду отправляет данные на сервер), используя встроенный в Python модуль socket.

Task_3_1_server.py Task_3_1_client.py Используя encode() и decode()

Task_3_2_server.py Task_3_2_client.py Используя pickle - де/сериализация произвольных объектов.

Task_3_3_server.py Task_3_3_client.py Используя Google Protocol Buffers - де/сериализация определенных структурированных данных, а не произвольных объектов Python


# РЕЗУЛЬТАТ РАБОТЫ:

# Task_1:

![image](https://github.com/Triceratops228/Triceratops228-Timur_Gallyamov_20321_HMI_CPD/assets/146287277/cfa30b5c-538e-470c-aff3-c9a2ce57e5ff)

# Task_2:

![image](https://github.com/Triceratops228/Triceratops228-Timur_Gallyamov_20321_HMI_CPD/assets/146287277/529428d7-cda5-4a4d-8c96-578e96e54447)

# Task_3:

image.png

# ПОЯСНЕНИЕ:

# Task_1:

Каждую секунду на сервер посылается время жизни процессора

# Task_2:

Каждую секунду посылает реальное время(день недели, месяц, число, время, год)

# Task_3:

Каждую секунду на сервер с клиента посылается сериализованное протобафом сообщение  "Hello World!"

# ЛИСТИНГ:

# Task_1:

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

# Task_2:

# Серверная часть:

``` py
import socket
import time
import pickle

""" server = socket.socket()            # создаем объект сокета сервера
hostname = socket.gethostname()     # получаем имя хоста локальной машины
port = 8080                        # устанавливаем порт сервера
server.bind((hostname, port))       # привязываем сокет сервера к хосту и порту
server.listen(5)                    # начинаем прослушиваение входящих подключений

print("Server starts")

 
con, addr = server.accept()     # принимаем клиента
print("connection: ", con)
print("client address: ", addr)


while True:
    data = con.recv(1024)
    message = pickle.loads(data)
    print(message["Время"])    
    con.close()                    

print("Server ends")
server.close() """
HOST = '' 
PORT = 8080 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket: 
    socket.bind((HOST, PORT)) 
    socket.listen(1) 
    conn, addr = socket.accept() 
    with conn: 
        print("Connected") 
        while True: 
            recv_data = conn.recv(1024) 
            data = pickle.loads(recv_data) 
            print(' - '.join(*data.items()))
            #print(k, v)
```

# Клиентская часть:

``` py
import socket
import time
import pickle

client = socket.socket()            # создаем сокет клиента
hostname = socket.gethostname()     # получаем хост сервера
port = 8080                        # устанавливаем порт сервера
client.connect((hostname, port))    # подключаемся к серверу
while True:
    data={"Время":str(time.ctime(time.time()))}
    s_data = pickle.dumps(data)
    client.send(s_data)
    time.sleep(1)
client.close()
```

# Task_3:

# ПРОТО ФАЙЛ:

``` py
syntax = "proto3";
package pb;
message TempEvent{
    optional string message = 1;
}
```

# СЕРВЕРНАЯ ЧАСТЬ:

``` py
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
```

# КЛИЕНТСКАЯ ЧАСТЬ:

``` py
import socket
import sys
import time
import file_pb2

HOST, PORT = "localhost", 8080
example_msg = file_pb2.TempEvent()
example_msg.message = "Hello world!"
data = example_msg.SerializeToString()

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    while True:
        sock.sendall(data)
        time.sleep(1)
```