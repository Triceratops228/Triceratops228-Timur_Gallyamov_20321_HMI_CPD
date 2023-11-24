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
