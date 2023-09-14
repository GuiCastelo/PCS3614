import socket

PORT = 80

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = socket.gethostbyname("127.0.0.1") # Ainda nao sei oq colocar no host
        s.connect((host, PORT))
        data = input()
        s.send(bytes(data, 'UTF-8'))

if __name__ == '__main__':
    main()
