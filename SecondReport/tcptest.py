import socket, threading

#创建socket实例
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#对本机在公网的IP地址，5000端口进行监听
s.bind(('0.0.0.0',5000))
#最大连接数
s.listen(5)

def tcplink():
	#创建TCP连接实例
    sock, addr = s.accept()
    sock.send(b'Welcome!')
    #循环接收信息
    while True:
        msg = sock.recv(1024)
        if msg.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s'%msg.decode('utf-8')).encode('utf-8'))

#启动TCP连接线程
t = threading.Thread(target = tcplink, args = ())
t.start()
