import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", 55000))
server.listen(10)
print("The server is running, press Ctrl + C to abrupt")
while True:
    try:
        client, address = server.accept()
        print("Connected: ", address)
    except KeyboardInterrupt:
        server.close()
        break
    else:
        while True:
            data = client.recv(1024)
            print(str(data))
            client.send(data.upper())
server.close()
