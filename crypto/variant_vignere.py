import gmpy2
import sys
from random import randrange
import re
from collections import Counter
text_list=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'
cipherText = open('cipher.txt','r').read()
print sys.argv[1]
def inv(x):
    return gmpy2.invert(x,97)
def repeat():
	c = Counter()
	for i in range(len(cipherText)):
		s = cipherText[i:i+int(sys.argv[1])]
		c[s] = c[s] + 1
	print sorted(c.items(),key = lambda eachItem:eachItem[1],reverse=True)
def brute():
	for keylen in range(15,30):
		num = 0
		if len(cipherText)%keylen==0:
			num = len(cipherText)/keylen
		else:
			num = len(cipherText)/keylen+1
		L = []
		for i in range(num):
			start = i*keylen
			end = (i+1)*keylen
			s = cipherText[start:end]
			L.append(s)
		for start in range(keylen):
			for length in range(1,keylen-start):
				if length ==3 :
					c = Counter()
					ans = []
					for mylist in L:
						ans.append(mylist[start:start+length])
					Max = 0
					poss = ''
					for a in ans:
						c[a] = c[a] + 1
						if c[a] > Max:
							Max = c[a]
							poss = a
					print "_______________"
					# print (keylen,start,length,sorted(c.items(),key = lambda eachItem:eachItem[1],reverse=True))
					print (keylen,start,length,poss,Max)
def findonekey(s,to):
	indexto=text_list.index(to)
	indexs=text_list.index(s)
	return inv(indexs)*indexto%97
def splitInto():
	cnt = 0
	fuckthistext = open('this_is_21.txt','r').read()
	for i in range(len(fuckthistext)):
		if i%29==0:
			print "012345678901234567890123456789here is the {0}".format(cnt)
			print fuckthistext[i:i+29]
			cnt += 1
splitInto()
# repeat()
# print [i.start() for i in re.finditer('{gY', cipherText)]
# brute()
# print findonekey('u','B')
# print findonekey('r','y')
# print findonekey('{','t')
# print findonekey('g','h')
# print findonekey('Y','e')
# # print findonekey('g','h')
# # print findonekey('e','Y')
# # print findonekey('Y','e')
# # print findonekey('u','A')
# # print findonekey('r','s')
# # print findonekey(')','s')
# # print findonekey(',','a')
# # print findonekey('y','y')
# # print findonekey('P','i')
# # print findonekey('T','n')
# # print findonekey('\t','g')
# print findonekey('Y',' ')
# print findonekey('b','g')
# print findonekey(';','o')
# print findonekey('8','e')
# print findonekey('5','s')
# print findonekey('S',',')
# print findonekey('V','i')
# print findonekey('7','y')
# print findonekey('N','c')
# print findonekey('b','l')
# print findonekey('9','t')
# print findonekey('2','s')
# print findonekey('H','l')
# print findonekey('5','e')
# print findonekey('K','h')
# print findonekey('L','i')
# print findonekey('H','t')
# print findonekey('`','o')
# # print findonekey('R','y')
# print findonekey(':','n')
# print findonekey('z','l')
# print findonekey('5','s')
# print findonekey('Q','a')
# print findonekey('l','s')
# print findonekey('W','e')
# print findonekey('T','c')
print findonekey('o','c')
print findonekey(':','e')
print findonekey('|','n')
print findonekey('k','t')
print findonekey('\'','u')
print findonekey('y','r')
print findonekey('^','y')
# # ),yPT\tYb
# ),yPT\tYb
# print findonekey()




