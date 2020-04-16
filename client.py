"""
创建一个tcp客户端
"""

from socket import *

# 创建socket
tcp_Cli_Sock = socket(AF_INET, SOCK_STREAM)

# 获取host和port
host = '127.0.0.1'
port = 8888

# 建立连接
tcp_Cli_Sock.connect((host, port))

while True:
    msg = input('> ')
    tcp_Cli_Sock.send(msg.encode('utf-8'))
    msg = tcp_Cli_Sock.recv(1024)
    tcp_Cli_Sock.close()

    print(msg.decode('utf-8'))

