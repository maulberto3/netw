def main():

    from ftplib import FTP
    from pprint import pprint
    from random import randint
    from time import sleep
    from datetime import datetime as dti

    # SIMPLE FTP standard scanner

    import socket as s

    def rand_adr():
        # https://www.csestack.org/different-classes-of-ip-address/
        return f'{randint(0,223)}.{randint(0,223)}.{randint(0,223)}.{randint(0,223)}'

    while True:
        # kill in unix with ps aux | grep <name of script> && kill <PID>
        print()
        adr = rand_adr()
        print(f'Trying {adr}...')
        try:
            with FTP(
                    adr, timeout=0.5
            ) as ftp_conn:  # connect to host, default port  # ftp.us.debian.org
                ftp_conn.set_debuglevel(2)
                print(ftp_conn.getwelcome())
                # ftp_conn.login()  # user anonymous, passwd anonymous@
                # ftp_conn.dir()
            with open('ftp_ok_anon_hosts.txt', 'a') as file:
                file.write(adr + '\n' + ' ' + ' ' + dti.now().strftime('%b-%d-%Y %T'))
        except BaseException as e:
            print(e)


if __name__ == '__main__':
    main()