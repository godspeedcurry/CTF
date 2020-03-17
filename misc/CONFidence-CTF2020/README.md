#### GPIO_tap

I solve this problem a little tricky.

1. After reading some manuals, I gradually knew the number in the given file.

2. We can directly put this number into a set and get `set([4, 17, 18, 22, 23, 24, 25])`

3. google raspi and GPIO  and I can get some info about Pin and number.

4. Then, I mark each wire on the picture to get a relationship.

5. D4-23

   D5-17

   D6-18

   D7-22

6. I read the source file carefully and find the first line only appears once. Just delete it.

7. Then I find `25 -> HIGH` or `25 -> LOW` appears very regularly(16 lines). So I remove all of them.

8. I use what I get in step 5 to convert all the data into characters. I find `Welcome to p4ctf :)` in the file but I can't find the flag.

9. Fortunately, I find a book wrote that `rs-HIGH` means 'text mode' and `rs-LOW` means  'command-mode'

10. For data after `25 -> HIGH`  and not after `25 -> LOW`，I extract them from the file and translate them.

11. ```python
    import re
    ans = ''
    def convert(string):
    	if string == 'LOW':
    		return '0'
    	else:
    		return '1'
    
    with open('1.txt') as f:
    	ans = f.read().strip().split('\n')
    ans = [convert(x.split(' -> ')[1]) for x in ans if len(x)]
    
    def func(mylist):
    	s = ''.join(ans)
    	test = ''
    	for i in range(0,len(s),4):
    		test += s[i+mylist[0]] + s[i+mylist[1]] + s[i+mylist[2]] + s[i+mylist[3]]
    	flag = ''
    	for i in range(0,len(test),8):
    		flag += chr(int(test[i:i+8],2))
    	print (flag)
    func([2,1,0,3])
    ```

12. I get `Welcome to p4ctf :) !!u4OI}rp{_tp4G_mPpwa`

13. I don't know if I am in the wrong direction so I just guess the flag to solve the problem quickly.

```
p4{GPIO_t4p_warmup!!}
p4{GPIO_tap_w4rmup!!}
p4{GpIO_taP_w4rmup!!}
p4{GpIO_tap_w4rmuP!!}
p4{GpIO_t4p_warmuP!!}
p4{GPIO_t4p_warmup!!}
p4{GPIO_t4p_warmup} <- right one!
p4{GPIO_tap_w4rmup}
p4{GpIO_taP_w4rmup}
p4{GpIO_tap_w4rmuP}
p4{GpIO_t4p_warmuP}
p4{GPIO_t4p_warmup}
```

13. Finally, I get the flag.

14. After submitting the flag, I know that the number before each character means order. 

15. ```python
    mylist = [(0xC0,'u'),(0x81,'4'),(0x86,'O'),(0x85,'I'),(0xC2,'}'),(0x8E,'r'),(0xC1,'p'),(0x82,'{'),(0x87,'_'),(0x88,'t'),(0x80,'p'),(0x89,'4'),(0x83,'G'),(0x8B,'_'),(0x8F,'m'),(0x84,'P'),(0x8A,'p'),(0x8C,'w'),(0x8D,'a')]
    mylist.sort(key=lambda x :x[0])
    print (mylist)
    flag = ''
    for x in mylist:
    	flag += x[1]
    print (flag)
    [(128, 'p'), (129, '4'), (130, '{'), (131, 'G'), (132, 'P'), (133, 'I'), (134, 'O'), (135, '_'), (136, 't'), (137, '4'), (138, 'p'), (139, '_'), (140, 'w'), (141, 'a'), (142, 'r'), (143, 'm'), (192, 'u'), (193, 'p'), (194, '}')]
    p4{GPIO_t4p_warmup}
    ```



![](https://tva1.sinaimg.cn/large/00831rSTly1gcxa709phrj30u00vdgyj.jpg)

