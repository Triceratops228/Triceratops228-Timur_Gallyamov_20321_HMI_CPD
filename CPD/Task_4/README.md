# Задание:

Клиент отправляет видео на PySide6 сервер, где проиходит отображение этого видео в виджете.

# Результат:

Изображение с вебкамеры передающееся на сервер

# Пояснение:

Берет картинку с вебкамеры кодирует ее и отправляет на сервер там декодирует и выводит изображение 

# Листинг:

# Серверная часть:

``` py
import sys
from tkinter import Label
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtNetwork import QTcpServer, QTcpSocket, QHostAddress
import video_pb2 
class VideoServer():
    def __init__(self):
        self.server = QTcpServer()
        self.server.listen(address=QHostAddress.Any,port=5252)
        self.message = video_pb2.Video()
        self.server.newConnection.connect(self.connect)
        self.mainWin = QMainWindow()
        self. lbl = QLabel()
        self.mainWin.setCentralWidget(self.lbl)
        self.lbl.show()
        self.mainWin.show()
        print('Server started')

    def connect(self):
        self.connection = self.server.nextPendingConnection()
        self.connection.readyRead.connect(self.show_frames)
        print(f'Connected to {self.connection}')

    def show_frames(self):
        frame_data = self.connection.readAll().data()
        self.message.ParseFromString(frame_data)
        pixmap = QPixmap()
        pixmap.loadFromData(self.message.video_data)
        self.lbl.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    video_server = VideoServer()
    sys.exit(app.exec_())
```

# Клиентская часть:

``` py
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
```

# Прото часть:

``` py
syntax = "proto3";

message Video {
   optional bytes video_data = 1;
   optional int32 id = 2;
}
```
