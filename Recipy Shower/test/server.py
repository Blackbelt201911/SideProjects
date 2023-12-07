import threading
import socket
import random 

PORT = 5050
SERVER = socket.gethostname()
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

random.seed(2)

count = random.randint(1, 99999999999999)

realCount = str(count)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(ADDR)

clients = set()
clients_lock = threading.Lock()


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} Connected")

    try:
        connected = True
        while connected:
            msg = conn.recv(1024).decode(FORMAT)
            if not msg:
                break

            if msg == DISCONNECT_MESSAGE:
                connected = False

            file = open("Recipe."+realCount+"txt","w")

            file.writelines(msg)
            
            file.close

            print(f"[{addr}] {msg}")
            with clients_lock:
                for c in clients:
                    c.sendall(f"[{addr}] {msg}".encode(FORMAT))

    finally:
        with clients_lock:
            clients.remove(conn)

        conn.close()


def start():
    print('[SERVER STARTED]!')
    
    server.listen()

    while True:
        conn, addr = server.accept()
        with clients_lock:
            clients.add(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


start()
