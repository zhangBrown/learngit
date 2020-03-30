import socket
import sys
import threading


def send_msg(udp_socket):
    ipdress = input("请输入发送的ip地址")
    if len(ipdress) == 0:
        ipdress = "127.0.0.1"
        print("默认地址%s" % ipdress)
    port = input("请输入发送的端口号")
    if len(port) == 0:
        port = 8080
        print("默认端口%s" % port)
    content = input("请输入发送的内容")
    udp_socket.sendto(content.encode(), (ipdress, int(port)))


def rev_msg(udp_socket):
    while True:
        rev_text, ipdress = udp_socket.recvfrom(1024)
        rev_text = rev_text.decode()
        print("由%s发来的%s" % (ipdress, rev_text))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("127.0.0.1", 8080))
    # 创建子线程，单独接收信息
    t1 = threading.Thread(target=rev_msg, args=(udp_socket, ))
    t1.setDaemon(True)  # 子线程守护主
    t1.start()

    while True:
        print("\n\n********************")
        print("*** 1、发送消息 *****")
        print("*** 2、退出系统 *****")
        print("********************")

        num = int(input("请输入需要选项\n"))
        if num == 1:
            send_msg(udp_socket)
        else:
            print("退出系统中")
            print("退出成功")
            udp_socket.close()
            break


def tcp_client():
    """文件下载器-客户端"""
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect(("127.0.0.1", 8081))

    file_name = input("输入要下载的文件名")
    tcp_socket.send(file_name.encode())

    with open("./" + file_name, "wb") as file:
        while True:
            file_data = tcp_socket.recv(1024)
            if file_data:
                file.write(file_data)
            else:
                break

    tcp_socket.close()


def tcp_server():
    """文件下载器-服务端"""
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_socket.bind(("", 8081))
    tcp_socket.listen(128)
    while True:
        new_sock, ip_port = tcp_socket.accept()

        recv_data = new_sock.recv(1024)
        file_name = recv_data.decode()

        try:
            with open(file_name, "rb") as ft:
                while True:
                    file_data = ft.read(1024)
                    if file_data:
                        new_sock.send(file_data)
                    else:
                        break

        except Exception as msg:
            print("下载失败%s" % file_name)
        else:
            print("下载成功")
        new_sock.close()

    tcp_socket.close()


class WebService(object):
    def __init__(self, port):
        web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        web_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        web_socket.bind(("", port))
        web_socket.listen(128)
        self.web_socket = web_socket

    def start(self):
        print("启动成功")
        while True:
            new_socket, ip = self.web_socket.accept()
            print(ip)
            self.res_handler(new_socket)
        self.web_socket.close()

    def res_handler(self, new_socket):
        data = new_socket.recv(1024)
        if not data:
            print("客户端已经下线")
            new_socket.close()
            return
        res_line = "HTTP/1.1 200 OK\r\n"
        res_header = "Server: Python/2.1\r\n"
        res_blank = "\r\n"
        res_body = "hello World"
        res = res_line + res_header + res_blank + res_body

        new_socket.send(res.encode())
        new_socket.close()


def main1():
        """linux上启动"""
        parm = sys.argv
        if len(parm) !=2:
            print("启动失败，格式错误")
            return
        if not parm[1].isdigit():
            print("启动失败，端口号不是数字")
            return
        port = int(parm[1])

        ws = WebService(port)
        ws.start()

if __name__ == '__main__':
    main()

