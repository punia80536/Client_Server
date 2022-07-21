import socket
PORT = 6000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as so:
    so.bind(("127.0.0.1",PORT))
    so.listen()
    con,add = so.accept()
print(f"connection has been estblished{add}")
con.send(b"pc under maintenance")


            
        