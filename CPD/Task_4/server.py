import sys
from tkinter import Label
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtNetwork import QTcpServer, QTcpSocket, QHostAddress
import video_pb2  # Импортируем сгенерированный protobuf-класс
import cv2
import struct

class VideoServer():
    def __init__(self):
        self.server = QTcpServer()
        if not self.server.listen(address=QHostAddress.Any, port=5252):
            print("Unable to start the server: %s." % self.server.errorString())
        print('Server started')
        self.message = video_pb2.Video()
        self.server.newConnection.connect(self.new_connection)
        self.mainWin = QMainWindow()
        self. lbl = QLabel()
        self.mainWin.setCentralWidget(self.lbl)
        self.lbl.show()
        self.mainWin.show()

    def new_connection(self):
        self.connection = self.server.nextPendingConnection()
        self.connection.readyRead.connect(self.process_frame)
        print(f'Connected to {self.connection}')

    def process_frame(self):
        # Десериализация protobuf-сообщения
        data = bytes()
        payload_size = struct.calcsize("q")
        while len(data) < payload_size:
            data += self.connection.readAll().data()
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("q", packed_msg_size)[0]
        while len(data) < msg_size:
            data += self.connection.readAll().data()
        frame_data = data[:msg_size]
        self.message.ParseFromString(frame_data)
        pixmap = QPixmap()
        pixmap.loadFromData(self.message.video_data)
        self.lbl.setPixmap(pixmap)
        # Получаем видео данные и выполняем необходимую обработкa


if __name__ == "__main__":
    app = QApplication(sys.argv)
    video_server = VideoServer()
    sys.exit(app.exec())