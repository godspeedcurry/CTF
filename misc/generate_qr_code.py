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
