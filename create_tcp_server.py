# 创建通用TCP服务器的一般伪代码

from socket import *

# 以下均为伪代码
ss = socket()  #  创建服务器套接字
ss = bind()  #  套接字与地址绑定
ss = listen()  #  监听连接
inf_loop:  #  服务器无限循环
    cs = ss.accept()  #  接受客户端连接
    comm_loop:  #  通信循环
        cs.recv()/cs.send()  #  对话（接收/发送）
    cs.close()  #  关闭客户端套接字
ss.close()  #  关闭服务器套接字#（可选）
