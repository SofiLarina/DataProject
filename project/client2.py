import socket
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Connected to server.")

client.connect(("localhost", 5002))
name = input("Enter your name: ")

def recv_message():
    while True:
        message = client.recv(1024).decode()
            print("\n" + message)

thread = Thread(target=recv_message, daemon=True)
thread.start()

while True:
    msg = input("Enter your message: ")
    if msg == "quit":
        break
    client.send((name + ": " + msg).encode())

client.close()


# переносим код из первого во второй клиент