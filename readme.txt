如果要在windows筆電與樹梅派之間，建立socket服務的TCP/IP連線，
則WINDOWS筆電作為CLIENT，RPi作為server，會是比較好的選擇。

因此RPi要先執行server.py，再換windows執行client.py。
    socket.AF_INET: IPv4 (Default)
    socket.SOCK_STREAM: TCP (Default) 

client傳文字"$100"
server5傳文字"apple"