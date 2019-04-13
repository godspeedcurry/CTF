import requests
back_word = ['swp','swn','swo']
houzhui = ['php','txt','html','xml','bak']
name = ['config','index','flag','practice','DDCTF','workspace','modules','www','deng379','Desktop','data']
for x in name:
	for y in houzhui:
		for z in back_word:
			for i in range(2):
				if i==0:				
					ans = '.'+x+'.'+y+'.'+z
				else:
					ans = x+'.'+y+'.'+z
				# print ans
				url = 'http://117.51.150.246/%s'%(ans)
				# print url
				r = requests.get(
					url
					)

				if r.status_code == 200:
					print url
