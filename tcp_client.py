"""
TCP套接字编程 客户端
"""
from socket import *

# 服务端地址
ADDR = ('127.0.0.1', 8888)

# 1. 使用默认值--->tcp
tcp_socket = socket()

# 2. 发起链接
tcp_socket.connect(ADDR)

# 3. 发送接收消息
while True:
    msg = input('>>')
    if not msg:
        break
    tcp_socket.send(msg.encode())


# 4. 关闭套接字
tcp_socket.close()
