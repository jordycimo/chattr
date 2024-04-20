import threading
import socket

port = 8088

username = input("username: ")

def main():
    sock = socket.socket()
    sock.bind((socket.gethostname(),8088))
    print ("socket bound to %s" %(port)) 
    sock.listen(5)
    print ("socket is listening")
    c, addr = sock.accept()	
    print ("connection from ", addr)
    
    t = threading.Thread(target=sock_loop, args=(c,))
    t.start()

    c.send("> ".encode()) # initial > to signify they are connected and ready to send
    
    while True:
        user_input = f"[{username}]: "+input("> ")+"\n\r"
        c.sendall(user_input.encode())  # maybe send some stuff?

def sock_loop(sock):
    while True:
        msg = ""
        while True:
            data = sock.recv(1024)
            msg += data.decode()
            if "\n" in msg:
                sock.send("> ".encode())
                print(msg)
                break

if __name__ == "__main__":
    main()