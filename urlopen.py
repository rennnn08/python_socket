import socket
import sys
def main():
    mes='GET / HTTP1.1\r\n'
    mes+='Connection: close\r\n'
    mes+='\r\n'

    url = sys.argv

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((url[1],80))

    s.send(mes.encode("utf-8"))

    data_sum = ''

    while True:
        data = s.recv(1024).decode("utf-8") 
        data_sum = data_sum + data 
        if not data:
            break

    s.shutdown(socket.SHUT_RDWR)
    s.close()

    with open ('index.html', 'w', encoding='utf-8') as o:
        o.write(data_sum)

if __name__ == '__main__':
    main()