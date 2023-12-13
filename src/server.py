import socket
import os
import time
import threading

PORT = 80
MAX_LINE = 512
MAX_PENDING = 5

def main():
    if socket.has_dualstack_ipv6():
        family = socket.AF_INET6
        dualstack = True
    else:
        family = socket.AF_INET6 if input('Inicializar servidor para conexões IPV6?(y/n): ') == 'y' else socket.AF_INET
        dualstack = False
    with socket.create_server(('', PORT), backlog=MAX_PENDING, family=family, dualstack_ipv6=dualstack) as s:
        threads = []
        try:
            while True:
                conn, addr = s.accept()
                t = threading.Thread(target=get_connection_file, args=(conn, addr))
                t.start()
                threads.append(t)
        except KeyboardInterrupt:
            pass
        finally:
            s.close()
            for t in threads:
                t.join()

def get_connection_file(conn: socket, addr: any):
    print(f'Conexão estabelecida para cliente {addr[0]} na Thread {threading.current_thread().ident}')
    request = conn.recv(MAX_LINE)
    request = str(request, 'UTF-8')
    filename = f'.{request.split(" ")[1]}'
    try:
        results = find_file(filename)
        response = f'HTTP/1.1 200 OK\r\nContent-Length:{results["size"]}\r\nContent-Type:text/html\r\n\r\n{results["bytes"].decode()}'
        response = bytes(response, 'UTF-8')
    except FileNotFoundError:
        response = b'HTTP/1.1 404 ERRO\r\n\r\n'
    except:
        response = b'HTTP/1.1 500 ERRO\r\n\r\n'
    finally:
        # Time sleep para simular resposta demorada
        time.sleep(10)
        conn.sendall(response)
        conn.close()

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
