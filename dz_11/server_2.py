import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

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
                if data.decode("utf-8") == "Hello" \
                or data.decode("utf-8") == "Hello!" \
                or data.decode("utf-8") == "Hi" \
                or data.decode("utf-8") == "Hi!":
                    client.send("How can I help you?".encode("utf-8"))
                elif data.decode("utf-8") == "Help me!":
                    client.send("What exactly do you want me to help you?".encode("utf-8"))
                elif data.decode("utf-8") == "How can I disconnect this server?":
                    client.send("Press Ctrl+C to abrupt".encode("utf-8"))
                else:
                    client.send("I'm tired, and you're annoying me. Good bye!".encode("utf-8"))
                    raise server.close()
