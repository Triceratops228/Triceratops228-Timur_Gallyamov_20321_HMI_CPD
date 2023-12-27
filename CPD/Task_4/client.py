import cv2
import socket
from PySide6.QtCore import *
from PySide6.QtNetwork import *
import video_pb2
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Подключаем сокет к порту, через который прослушивается сервер
server_address = ('localhost', 5050)
print('Подключение к {} порт {}'.format(*server_address))


sock.connect(server_address)
print('Подключено')
vid = cv2.VideoCapture(0)
message = video_pb2.Video()
while True:
    ret, frame = vid.read()
    #compressed_frame = cv2.resize(frame, (176, 144), interpolation=cv2.INTER_AREA)
    _, img_encoded = cv2.imencode('.jpg', frame)
    string_data = img_encoded.tobytes()
    message.video_data = string_data
    serialized_message = message.SerializeToString()
    print(len(serialized_message))
    message1 = len(serialized_message).to_bytes(4, byteorder='big') + serialized_message
    sock.sendall(message1)
    cv2.imshow('client', frame)
vid.release()