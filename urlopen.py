import socket
import sys
from ssl import wrap_socket
from contextlib import closing

def main():
    url = sys.argv

    mes='GET / HTTP/1.1\r\n'
    mes+='Host:' + url[1] + '\r\n'
    mes+='Connection: close\r\n\r\n'

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((url[1],80))

    s.send(mes.encode("utf-8"))

    data_sum = ''
    flag = False

    while True:
        data = s.recv(1024).decode("utf-8", 'ignore') 
        print(data)
        split_data = data.split('\r\n')
        for d in split_data:
            if flag:
                data_sum = data_sum + d
            if 'charset' in d:
                flag = True
        
        if not data:
            break

    s.shutdown(socket.SHUT_RDWR)
    s.close()

    with open ('index.html', 'w', encoding='utf-8') as o:
        o.write(data_sum)

if __name__ == '__main__':
    main()