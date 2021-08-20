from pprint import pprint
import socket
import sys

# reomote connect www

if __name__ == '__main__':

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created')
    except socket.error as err:
        print("Failed to crate a socket")
        print("Reason: %s" % str(err))
        sys.exit()

    target_host = 'www.python.org'  # '127.0.0.1'
    target_port = 80  # 8080

    try:
        # sock.connect((target_host, int(target_port)))
        sock = socket.create_connection((target_host, int(target_port)), timeout=1000)
        print("Socket Connected to %s on port: %s" %
              (target_host, target_port))
        sock.shutdown(2)
    except socket.error as err:
        print("Failed to connect to %s on port %s" %
              (target_host, target_port))
        print("Reason: %s" % str(err))
        sys.exit()
