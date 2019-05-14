import os
import hashlib
from pwn import *
dct = dict()
dct1 = dict()
for i in range(256*256*16):
        hash = hashlib.sha384()
        ss = str(i)
        hash.update(ss.encode('utf-8'))
        s =hash.hexdigest()
        dct[ss] = s
        dct1[s[-6:]] = ss
for i in range(100):
    r = remote('10.214.24.188',2019)
    r.recvuntil('sha384(str).hexdigest()[-6:] == ')
    ans = r.recvline()[:-1]
    r.recvuntil('Give me str:')

    if dct1.get(ans):
        myans = dct[dct1[ans]]
        print dct1[ans]
        r.sendline(dct1[ans])
        r.interactive()
    r.close()
