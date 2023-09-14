import socket

PORT = 80
MAX_LINE = 256
MAX_PENDING = 5

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((socket.INADDR_ANY, PORT))
        s.listen(MAX_PENDING)
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(MAX_LINE)
                print(str(data, 'UTF-8'))
                if not data:
                    break

if __name__ == '__main__':
    main()
