import socket

MAX_LINE = 256

def main():
    # Host deve ser passado via input
    address = input("Digite o host a ser buscado, no formato hostname:port/file: ")

    hostname = address.split(':')[0]
    port = address.split(':')[-1].split('/')[0]
    file = address.split('/', 1)[-1]

    print(hostname, port, file)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = socket.gethostbyname(hostname)
        s.connect((host, int(port)))
        data = f'GET /{file} HTTP/1.1\r\nHost:{host}\r\n\r\n'
        s.send(bytes(data, 'UTF-8'))
        response = s.recv(MAX_LINE)
        print(response)
        s.close()

if __name__ == '__main__':
    main()
