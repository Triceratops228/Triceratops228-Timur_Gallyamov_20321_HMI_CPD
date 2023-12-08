# ЗАДАНИЕ:

Используя Google Protocol Buffers - де/сериализация определенных структурированных данных, а не произвольных объектов Python

# РЕЗУЛЬТАТ РАБОТЫ:

![image](https://github.com/Triceratops228/Triceratops228-Timur_Gallyamov_20321_HMI_CPD/assets/146287277/df0b1c66-c725-4799-a83d-0d3bc03f7eb2)

# ПОЯСНЕНИЕ:

Каждую секунду на сервер с клиента посылается сериализованное протобафом сообщение  "Hello World!"

# ЛИСТИНГ:

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
