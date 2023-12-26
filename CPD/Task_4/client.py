import cv2
import socket
from PySide6.QtCore import *
from PySide6.QtNetwork import *
import video_pb2

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5252)

sock.connect(server_address)
print('Подключено')
video = cv2.VideoCapture(0)
message = video_pb2.Video()

while True:   
    _, frame = video.read()
    pressed_frame = cv2.resize(frame, (144, 144), interpolation=cv2.INTER_AREA)
    _, img_encoded = cv2.imencode('.jpg', pressed_frame)
    data = img_encoded.tobytes()
    message.video_data = data
    serialized_message = message.SerializeToString()
    print(len(serialized_message))
    sock.sendall(serialized_message)
    cv2.imshow('client', frame)
vid.release()