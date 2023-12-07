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
