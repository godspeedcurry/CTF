from PIL import Image
import numpy as np
ans = []
for i in range(1,442):
	filename = '{0}.png'.format(i)
	with open(filename,'rb') as f:
		siz =  (len(f.read()))
		if siz == 235:
			ans.append(1)
		else:
			ans.append(0)
print ans
cnt = 0
img = Image.new("RGB",(21,21))
for i in range(21):
	for j in range(21):
		if ans[i*21+j]:
			img.putpixel((i,j),(0,0,0))
		else:
			img.putpixel((i,j),(255,255,255))
print (np.array(img))
img.show()

# *ctf{half_flag_&_the_rest}



# 高级一点的版本，包含二维码识别，会生成一张图片在当前目录下

#coding=utf-8
from __future__ import print_function
from PIL import Image
from pwn import *
def filter(mymap):
    mymap = mymap.replace('█','1')
    mymap = mymap.replace(' ','0')
    mymap = mymap.replace('\n','')
    mymap = mymap.replace('.','')
    return mymap

def qrdecode():
    from pyzbar import pyzbar
    img = Image.open('tmp.png')
    txt_list = pyzbar.decode(img)
    ans = ''
    for txt in txt_list:
        barcodeData = txt.data.decode("utf-8")
        ans += barcodeData
    print (ans)

def gen_qrcode(mymap):
    import math
    from pyzbar.pyzbar import decode  # QR decoder
    from PIL import Image
    from itertools import chain

    mymap = filter(mymap)
    mymap = [x=='1' for x in mymap]
    height = int(math.sqrt(len(mymap)))
    width = int(math.sqrt(len(mymap)))
    size = (height, width)
    im = Image.new('1', size)
    im.putdata(mymap)
    im = im.resize((height*10,width*10),Image.ANTIALIAS)
    im.save('tmp.png',quality=100)


def Text2QrcodeBinStr(text):
    import qrcode
    qr = qrcode.QRCode(box_size=2, border=4)
    qr.add_data(text)
    qr.make(fit=True)
    im = qr.make_image().convert('1')
    return (''.join(['1' if metadata==255 else '0' for metadata in im.getdata() ]))


def GetQrcodeBinStr2Text(targetBinaryString):
    gen_qrcode(targetBinaryString)
    qrdecode()

def main():
    binstr = Text2QrcodeBinStr('aaa')
    GetQrcodeBinStr2Text(binstr)
if __name__ == '__main__':
	main()
