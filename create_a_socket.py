# 创建套接字的手法:第三个参数protocol通常省略
# socket(socket_family, socket_type, protocol=0)


from socket import *


# 创建tcp套接字的方法
tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 创建udp套接字的方法
udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
