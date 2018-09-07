import time, functools
def metric(fn):
	@functools.wraps(fn)
	def wrapper(*args,**kw):
		print('%s executed in %s ms' % (fn.__name__, 10.24))
		return fn(*args,**kw)
	return wrapper
	
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;
f = fast(11, 22)
f = fast(11, 22)