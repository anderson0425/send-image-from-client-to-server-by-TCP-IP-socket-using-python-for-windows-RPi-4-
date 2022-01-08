import socket

HOST = '192.168.43.2'  #FIXME:
PORT = 8000

#client傳給server的文字訊息
clientMessage = '$100'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET:表示使用的是 IPv4
# SOCK_STREAM:表示使用的是 TCP
#因此這個SOCKET服務是一個TCP/IP服務

client.connect((HOST, PORT))
print("connect!")
client.sendall(clientMessage.encode())

#client接收來自server的data
serverMessage = str(client.recv(1024), encoding='utf-8')

#印出server傳給client的data
print('message sent from server:', serverMessage)

client.close()