import zlib
import struct
crc32key = 0xF37A5E12 #补上0x，winhex下copy hex value。
data = bytearray(b'\x49\x48\x44\x52\x00\x00\x01\x00\x00\x00\x00\x00\x08\x02\x00\x00\x00')   #winhex下copy grep hex。
n = 8192 #理论上0xffffffff,但考虑到屏幕实际/cpu，0x0fff就差不多了
for w in range(n):#高和宽一起爆破
    width = bytearray(struct.pack('>i', w))#q为8字节，i为4字节，h为2字节
    for h in range(n):
        height = bytearray(struct.pack('>i', h))
        for x in range(4):
            data[x+4] = width[x]
            data[x+8] = height[x]
        crc32result = zlib.crc32(data)
        if crc32result == crc32key:
            print(width,height)
