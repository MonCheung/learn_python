import hashlib

md5 = hashlib.md5()
md5.update('cjy19901126'.encode('utf-8'))
print(md5.hexdigest())
