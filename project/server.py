import socket
from threading import Thread
from working_with_db import registration, autorization

# создаем серверный сокет
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# привязываем его к адресу и порту
server.bind(("localhost", 5002))
# переводим сервер в режим прослушивания клиентов
server.listen(10)

print("Server is running...")

# set для клиентских сокетов
clients = set()

def menu(connection):
    while True:
        action = connection.recv(1024).decode()
        if action == "1":
            data = connection.recv(1024).decode().split(".")
            answer = registration(name=data[0], login=data[1], password=data[2])
            if answer:
                connection.send("1".encode())
            else:
                connection.send("2".encode())

        elif action == "2":
            data = connection.recv(1024).decode().split(".")
            answer = autorization(login=data[0], password=data[1])
            if not answer:
                connection.send("2".encode())
            else:
                connection.send(answer.encode())

                thread = Thread(target=chatting, args=(client_sock,), daemon=True)
                thread.start()

                break


# фукнция для обмена сообщениями
def chatting(cs):
    # цикл для принятия и отправки сообщений
    while True:
        # получаем сообщения от клиента
        try:
            message = cs.recv(1024).decode()
        except ConnectionResetError:
            clients.remove(cs)
            break

        # проходимся циклом по клиентам во множестве клиентов
        for client in clients:
            # отправляем сообщения, присланные клиентом всем остальным
            client.send(message.encode())

# цикл для принятия подключения клиента
while True:
    # принимаем подключение
    client_sock, client_addr = server.accept()
    print(f"Client {client_addr} is connected.")

    # во множество клиентов добавляем сокет подключенного клиента
    clients.add(client_sock)
    print(clients)

    menu(client_sock)