import sys
from tkinter import Label
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtNetwork import QTcpServer, QTcpSocket, QHostAddress
import video_pb2 
class VideoServer():
    def __init__(self):
        self.server = QTcpServer()
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