import serial,binascii,_thread
 
ser = serial.Serial()
i = 0

#打开串口
def port_open():
    ser.port = "com4"       #设置端口号
    ser.baudrate = 115200   #设置波特率
    ser.bytesize = 8        #设置数据位
    ser.stopbits = 1        #设置停止位
    ser.parity = "N"        #设置校验位
    ser.timeout = 0.5       #设置read超时时间
    ser.open()              #打开串口,要找到对的串口号才会成功
    if(ser.isOpen()):
        print("打开成功")
    else:
        print("打开失败")
 
#关闭串口
def port_close():
    ser.close()
    if (ser.isOpen()):
        print("关闭失败")
    else:
        print("关闭成功")

#发送数据
def send(send_data):
    if (ser.isOpen()):
        ser.write(send_data.encode('utf-8'))  #utf-8 编码发送
        #ser.write(binascii.a2b_hex(send_data))  #Hex发送
        print("发送成功",send_data)
    else:
        print("发送失败")
 
#接收数据
def read():
	msg=''
	while True:
		data = (ser.readline()).decode('utf-8')
		msg+=data
		print(msg)
 
if __name__ == "__main__":
    port_open()
    _thread.start_new_thread(read,())
    send(" World")
    while True:
        i = i+1