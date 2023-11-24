ЗАДАНИЕ:
Task_3_2_server.py Task_3_2_client.py Используя pickle - де/сериализация произвольных объектов.

РЕЗУЛЬТАТ РАБОТЫ:

![image](https://github.com/Triceratops228/Triceratops228-Timur_Gallyamov_20321_HMI_CPD/assets/146287277/529428d7-cda5-4a4d-8c96-578e96e54447)

Пояснение:

Каждую секунду посылает реальное время(день недели, месяц, число, время, год)

Листинг:

Серверная часть:

```import socket
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

Клиентская часть:
```
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
