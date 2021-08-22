from ftplib import FTP
from pprint import pprint
from random import randint
from time import sleep

# SIMPLE FTP standard

import socket as s

def rand_adr():
    return f'{randint(0,223)}.{randint(0,223)}.{randint(0,223)}.{randint(0,223)}'

with open('ftp_ok_hosts.txt', 'w+') as file:
    file.write(randint())

with open('ftp_ok_hosts.txt', 'w+') as file:
    file.write(randint())



for i in range(1000):
    adr = rand_adr()
    print(f'Trying {adr}...')
    try:
        with FTP(adr, timeout=1) as ftp_conn: # connect to host, default port  # ftp.us.debian.org
            ftp_conn.login()  # user anonymous, passwd anonymous@
            ftp_conn.dir()
            # with open('ftp_ok_hosts.txt', 'w+')
            # ftp.retrlines('LIST')  # list directory contents
            # ftp.cwd('debian')  # change into "debian" directory
            # ftp.nlst()
            # with open('README', 'wb') as fp:
            #     ftp.retrbinary('RETR README', fp.write)
            # ftp.quit()
    except BaseException as e:
        print()
        print(e)
