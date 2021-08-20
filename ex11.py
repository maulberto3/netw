import paramiko
import socket

# PUT DATA ABOUT YOUR SSH SERVER

# in cli 
# sudo /usr/bin/ssh-keygen -A
# systemctl start sshd
# systemctl status sshd

host = 'localhost'
username = 'maulberto3'
password = 'Mauvidgam55'

try:
    ssh_client = paramiko.SSHClient()
    #shows debug info
    paramiko.common.logging.basicConfig(level=paramiko.common.DEBUG)
    #The following lines add the server key automatically to the know_hosts file
    ssh_client.load_system_host_keys()
    # ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    response = ssh_client.connect(host, username=username)
    print('==> Connected with host on port 22', response)
    transport = ssh_client.get_transport()
    security_options = transport.get_security_options()
    print(security_options.kex)
    print(security_options.ciphers)

except paramiko.BadAuthenticationType as exception:
    print("BadAuthenticationException:", exception)
except paramiko.SSHException as sshException:
    print("SSHException:", sshException)
except socket.error as socketError:
    print("socketError:", socketError)
finally:
        print("closing connection")
        ssh_client.close()
        print("closed")