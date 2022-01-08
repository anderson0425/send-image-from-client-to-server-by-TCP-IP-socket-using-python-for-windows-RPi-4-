# -*- coding: utf-8 -*-

#Client 端傳送了一次訊息後便關閉了；
# 相較之下， Server 端持續開著等待 Client 端的請求。

import socket

#若用不同裝置但相同網域測試
HOST = '192.168.43.2'  #FIXME:修改成作為server的裝置的IP
PORT = 8000

#若只在某個裝置內部測試  # 127.0.0.1
#HOST = 'localhost'
#PORT = 1002

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET:表示使用的是 IPv4
# SOCK_STREAM:表示使用的是 TCP
#因此這個SOCKET服務是一個TCP/IP服務

server.bind((HOST, PORT))  ## 讓這個socket要綁到位址(ip/port)
#server.bind(('localhost', 1002))  # 127.0.0.1

server.listen(10)  
#server.listen()
# listen(backlog)
# backlog:操作系統可以掛起的最大連接數量。該值至少為1，大部分應用程序設為5就可以了


while True:
    print("server is waiting for request......................")

    conn, addr = server.accept() 
    # 接受遠程計算機的連接請求，建立起與client端之間的通信連接
    # conn是新的套接字對象，可以用來接收和發送數據。
    # address是client端的地址
    #socket會停在這一行，等待request，不會進入下一個迴圈

    #檢查ip
    print("server addr:  " + HOST)
    print("client addr:  " + addr[0])

    #-------------------------------------------------------------------
    # 開始接收圖片
    print('server begin receive image from client')
    img_file = open('./0.jpg', 'wb')  # 開始寫入圖片檔  #img_file = open('./0.jpg', 'w') 會出現TypeError: write() argument must be str, not bytes
    image_data = conn.recv(2048)  # stream-based protocol  # 接收遠端主機傳來的數據
    while image_data:  # 讀完檔案結束迴圈
        img_file.write(image_data)
        image_data = conn.recv(2048)
    img_file.close()
    conn.close()
    #-------------------------------------------------------------------

server.close()
print('server close')