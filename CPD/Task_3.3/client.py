import socket
import sys
import time
import file_pb2

HOST, PORT = "localhost", 8080
example_msg = file_pb2.TempEvent()
example_msg.message = "Hello world!"
data = example_msg.SerializeToString()

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    while True:
        sock.sendall(data)
        time.sleep(1)