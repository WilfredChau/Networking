"""
创建一个tcp服务器端
"""

from socket import *
import time

# 创建socket
tcp_Ser_Sock = socket(AF_INET, SOCK_STREAM)

# 获取host和port
host = '127.0.0.1'
port = 8888

# 绑定端口号
tcp_Ser_Sock.bind((host, port))

# 监听连接，设置最大连接数
tcp_Ser_Sock.listen(5)

# 进入无限循环
while True:
    print('waiting for connection...')

    # 接收客户端连接
    tcp_Cli_Sock, addr = tcp_Ser_Sock.accept()

    print('link address：%s' % str(addr))
    msg = tcp_Cli_Sock.recv(1024).decode('utf-8')
    tcp_Cli_Sock.send(msg.encode('utf-8'))

    # 关闭套接字
    tcp_Cli_Sock.close()
