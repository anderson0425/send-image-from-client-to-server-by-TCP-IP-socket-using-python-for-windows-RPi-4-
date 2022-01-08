import socket
import time

#client傳圖片給server
#server不做任何事

#若用不同裝置但相同網域測試
HOST = '192.168.43.2'  #FIXME:修改成作為server的裝置的IP
PORT = 8000

#若只在某個裝置內部測試  # 127.0.0.1
#HOST = 'localhost'
#PORT = 1002

#client傳給server的文字訊息
#clientMessage = '$100'

print("server addr:  " + HOST)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET:表示使用的是 IPv4
# SOCK_STREAM:表示使用的是 TCP
#因此這個SOCKET服務是一個TCP/IP服務

client.connect((HOST, PORT))  # 用來請求連接遠程服務器
print("connect!")

time1 = time.time()

#傳送圖片
#-------------------------------------------------------------------
print('client begin send image to server')
img_file = open("./0.jpg", "rb")   #FIXME:修改成自己的圖片路徑
image_data = img_file.read(2048)
while image_data:  # 讀完檔案結束迴圈
    client.send(image_data)
    image_data = img_file.read(2048)
img_file.close()
print("send img done")
#-------------------------------------------------------------------

time2 = time.time()
print("time cost: {}".format(time2-time1))

client.close()