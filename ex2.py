import paramiko
from getpass import getpass

# capturing ssh paramiko

HOSTNAME = '127.0.0.1'
PORT = 49862


def run_ssh_cmd(username, password, cmd, hostname=HOSTNAME, port=PORT):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.load_system_host_keys()
    ssh_client.connect(hostname, port, username, password)
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    print(stdout.read())


if __name__ == '__main__':
    username = 'maulberto3'
    password = 'Mauvidgam55'
    cmd = 'ls'
    run_ssh_cmd(username, password, cmd)