import socket
import threading


def recv_msg(new_socket):
    while True:
        res_data = new_socket.recv(1024)
        if res_data:
            res_text = res_data.decode()
            print(res_text)
        else:
            new_socket.close()
            break
    new_socket.close()


socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
socket_server.bind(("", 8082))

socket_server.listen(128)
while True:
    new_socket, ip_port = socket_server.accept()
    print(new_socket)

    recv_threading = threading.Thread(target=recv_msg, args=(new_socket,))
    recv_threading.setDaemon(True)
    recv_threading.start()

socket_server.close()