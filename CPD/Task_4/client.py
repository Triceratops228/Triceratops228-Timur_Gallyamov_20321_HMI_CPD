import cv2
import socket
from PySide6.QtCore import *
from PySide6.QtNetwork import *
import video_pb2
import struct
import time

def sendVideoDataToServer(self):
    print('send')



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Подключаем сокет к порту, через который прослушивается сервер
server_address = ('localhost', 5252)
print('Подключение к {} порт {}'.format(*server_address))

try:
    sock.connect(server_address)
    print('Подключено')
    vid = cv2.VideoCapture(0)
    message = video_pb2.Video()
    # Отправка данных
    while True:
        # Отправка данных
        ret, frame = vid.read()
        compressed_frame = cv2.resize(frame, (176, 144), interpolation=cv2.INTER_AREA)
        _, img_encoded = cv2.imencode('.jpg', compressed_frame)
        string_data = img_encoded.tobytes()
        

        # Заполняем protobuf-сообщение
        message.video_data = string_data

        # Отправляем данные на сервер
        serialized_message = message.SerializeToString()
        print(len(serialized_message))
        sock.sendall(struct.pack("q", len(serialized_message)) + serialized_message)
        cv2.imshow('client', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()

except ConnectionRefusedError:
    print('Подключение не установлено, сервер не отвечает')