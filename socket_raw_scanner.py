import socket

# quick way to test open ports

ip = 'www.google.com'
# portlist = [21, 22, 23, 80]
for port in [80, 443]:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    if result != 111:
        print(port, ":", result)
    sock.close()