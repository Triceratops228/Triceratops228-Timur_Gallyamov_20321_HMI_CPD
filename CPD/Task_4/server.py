import sys
from tkinter import Label
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtNetwork import QTcpServer, QTcpSocket, QHostAddress
import video_pb2  # Импортируем сгенерированный protobuf-класс
import cv2
import struct
import io

class VideoServer():
    def __init__(self):
        self.server = QTcpServer()
        if not self.server.listen(address=QHostAddress.Any, port=5050):
            print("Unable to start the server: %s." % self.server.errorString())
        print('Server started')
        self.message = video_pb2.Video()
        self.buffer = io.BytesIO()
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
        self.buffer.write(self.connection.readAll())
        data_size = len(self.buffer.getvalue())
        if data_size >= 4:
            # Получение размера сообщения из первых 4 байт
            message_size = int.from_bytes(self.buffer.getvalue()[:4], 'big')
            if data_size >= 4 + message_size:
                # Извлечение данных видео и их обработка
                self.message.ParseFromString(self.buffer.getvalue()[4:4 + message_size])
                pixmap = QPixmap()
                pixmap.loadFromData(self.message.video_data)
                self.lbl.setPixmap(pixmap)

                # Обрезаем буфер после успешной обработки сообщения
                self.buffer = io.BytesIO(self.buffer.getvalue()[4 + message_size:])

        # Получаем видео данные и выполняем необходимую обработкa


if __name__ == "__main__":
    app = QApplication(sys.argv)
    video_server = VideoServer()
    sys.exit(app.exec_())