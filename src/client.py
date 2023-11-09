import socket

MAX_LINE = 512

def main():
    # Host deve ser passado via input
    address = input("Digite o host a ser buscado, no formato hostname:port/file: ")

    hostname = ':'.join(address.split(':')[0:-1])
    port = address.split(':')[-1].split('/')[0]
    file = address.split('/', 1)[-1]

    try:
        family, _, _, _, host = socket.getaddrinfo(hostname, port, socket.AF_UNSPEC, socket.SOCK_STREAM)[0]
    except:
        print('Host não encontrado')
        exit()
    
    with socket.socket(family, socket.SOCK_STREAM) as s:
        try:
            s.connect(host)    
            print(f'Conexão feita usando {"IPV6" if family == socket.AF_INET6 else "IPV4"}')
            request = f'GET /{file} HTTP/1.1\r\nHost:{host}\r\n\r\n'
            s.send(bytes(request, 'UTF-8'))
            response = s.recv(MAX_LINE)
            print(f'Resposta: {response.decode()}')
            s.close()
        except ConnectionRefusedError:
            print('Conexão recusada pelo servidor')
            exit()

if __name__ == '__main__':
    main()
