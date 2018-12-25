#coding=utf-8
#File vigenere.py
## -*-  coding:utf8 -*-
import gmpy2
from random import randrange
text_list=' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\n'
# for ch in text_list:
#     print ord(ch)
alphabet = [text_list[i] for i in range(len(text_list))]

def inv(x):
    return gmpy2.invert(x,97)

def decode(cipherText):
    '''解密'''
    length = findKeyLen(cipherText) #得到密钥长度
    key = [78, 7, 75, 83, 42, 88, 40, 84, 95, 40, 71, 50, 12,  32, 76, 57, 15, 31,70,27,3,33,34,81,62,5,26,14,3] #解密密钥
    # key = findKey(cipherText,length) #找到密钥
    print key
    plainText = ''
    index = 0
    for ch in cipherText:
        plainIndex=text_list.index(ch)
        plainIndex*=key[index%len(key)]
        plainIndex%=97
        # index=text_list.index(ch)
        # Inverse = inv(key[index%length])
        # plainIndex = index*Inverse%97
        plainText += text_list[plainIndex]
        if (index%29==2):
            print text_list[plainIndex]
        index+=1
    return plainText
        
def openfile(fileName):
    '''读取文件'''
    file = open(fileName,'r')
    text = file.read()
    file.close();
    text = text.replace('\n','')
    return text

def findKeyLen(cipherText):
    '''寻找密钥长度'''
    length = 1
    maxCount = 0
    for step in range(1,30):#假定密钥长度在15到30之间
        count = 0
        for i in range(step,len(cipherText)-step):
            if cipherText[i] == cipherText[i+step]:
                 count += 1
        print(count)
        if count>maxCount:
            maxCount = count
            length = step
    print "ansKeyLen",length
    return length
def get_frequency():
    ans =  []
    plain=open('dict.txt','r').read() # TOEFL reading passage
    # print plain
    hits = [
        (text_list[i], plain.count(text_list[i]))
        for i in range(len(text_list))
        # if plain.count(text_list[i])
    ]
    ans = []
    for letter, frequency in hits:
        print ord(letter), frequency*1.0/len(plain)
        ans.append(frequency*1.0/len(plain))
    return ans
             

def countList(lis):
    '''统计列表中a-z出现的频率'''
    li = []
    alphabet = [text_list[i] for i in range(len(text_list))]
    for c in alphabet:
        count = 0
        for ch in lis:
            if ch == c:
                count+=1
        li.append(count/len(lis))
    return li
        
def textToList(text,length):
    '''按密钥长度将text分组'''
    textMatrix = []
    row = []
    index = 0 
    for ch in text:
        row.append(ch)
        index += 1
        if index % length ==0:
            textMatrix.append(row)
            row = []
    return textMatrix
#按行输出矩阵
def printTextMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
if __name__ == '__main__':
    cipherText = open('cipher.txt','r').read()
    print('====================')   
    plainText= decode(cipherText)
    open('this_is_21.txt','w').write(plainText)
    print('====================')
    print('plainText:\n',plainText)
