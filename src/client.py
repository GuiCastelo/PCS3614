import socket
import sys

PORT = 80

def main():
    # Host deve ser passado via linha de comando
    if(len(sys.argv) == 2):
        hostname = sys.argv[1]
    else:
        raise AttributeError('usage: simple-talk host')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = socket.gethostbyname(hostname)
        s.connect((host, PORT))
        data = input()
        while data:
            s.send(bytes(data, 'UTF-8'))
            data = input()

if __name__ == '__main__':
    main()
