# -*- coding: utf-8 -*-

#Client 端傳送了一次訊息後便關閉了；相較之下，我讓 Server 端持續開著等待 Client 端的請求。

#server要先執行，再執行client

#在這邊的話，我們什麼結果都沒有印出來，
# 我們只是啟動了 socker 的 server 端（伺服器） 在等待 client 端（客戶端）的訊息而已。

#一開始，在 Server 端，我們先設定好 Host 跟我們的 Port。
#然後server就會一直等待，等待對應於那個host跟port的client的request。

import socket

#一開始，在 Server 端，我們先設定好 Host 跟我們的 Port。
HOST = '192.168.43.2' #FIXME:
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET:表示使用的是 IPv4
# SOCK_STREAM:表示使用的是 TCP
#因此這個SOCKET服務是一個TCP/IP服務

server.bind((HOST, PORT))
server.listen(10)

while True:
    print("server is waiting for request......................")
    conn, addr = server.accept()

    #server接收來自client的data
    clientMessage = str(conn.recv(1024), encoding='utf-8')

    #印出client傳給server的data
    print('message sent from client:', clientMessage)

    #server傳給client的訊息
    serverMessage = 'apple'

    conn.sendall(serverMessage.encode())
    conn.close()