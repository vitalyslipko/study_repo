import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

    server.connect(("localhost", 55000))
    print("Connection to the server has been set")
    while True:
        string_data = input("Enter here: ")
        server.send(bytes(string_data, encoding="UTF-8"))
        received_data = server.recv(1024)
        print(received_data)
