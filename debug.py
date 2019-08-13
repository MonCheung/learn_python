from urllib import request

with request.urlopen('http://tqapi.mobile.360.cn/app/meizu/city/101010100') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
