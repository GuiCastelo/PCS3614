import socket
import os

PORT = 80
MAX_LINE = 256
MAX_PENDING = 5

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', PORT))
        s.listen(MAX_PENDING)
        conn, addr = s.accept()
        with conn:
            request = conn.recv(MAX_LINE)
            request = str(request, 'UTF-8')
            filename = f'.{request.split(" ")[1]}'
            try:
                results = find_file(filename)
                response = f'HTTP/1.1 200 OK\r\nContent-Length:{results["size"]}\r\nContent-Type:text/html\r\n\r\n{results["bytes"]}'
                response = bytes(response, 'UTF-8')
            except:
                response = b'HTTP/1.1 400 ERRO\r\n\r\n'
            finally:
                conn.sendall(response)
        s.close()

def find_file(filename):
    if os.path.isfile(filename):
        with open(filename, 'rb') as file:
            bytes_file = file.read()
        return {
            'size': os.path.getsize(filename),
            'bytes': bytes_file
        }
    else:
        raise FileNotFoundError(f'{filename} not found in the server')

if __name__ == '__main__':
    main()
