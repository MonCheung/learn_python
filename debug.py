import hashlib

sha1 = hashlib.sha1()
sha1.update('123456'.encode('utf-8'))
print(sha1.hexdigest())
