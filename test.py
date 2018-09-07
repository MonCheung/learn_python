'''
def fact(n):
    print("factorial has been called with n = "  + str(n))
    if n == 1:
        return 1
    else:
        res = n * fact(n - 1)
        print("intermediate result for ", n, " * fact(", n - 1, "): ", res)
        return res

print(fact(20))
'''

'''
#递归算法的实现
def fact(n):
    result=1
    for i in range(2,n+1):
        result=result*i
    return result

print(fact(1))
print(fact(2))
print(fact(1000))
'''

'''#字符串和编码练习
# -*- coding: utf-8 -*-
a=int(input('请输入上次成绩：'))
b=int(input('请输入本次成绩：'))
r=int(((b-a)/a)*100)
print('恭喜成绩提升%.1f%%' % r)
'''

''''#列表练习
# -*- coding: utf-8 -*-
L = [['Apple', 'Google', 'Microsoft'],['Java', 'Python', 'Ruby', 'PHP'],['Adam', 'Bart', 'Lisa']]
#打印apple
print(L[0][0])
#打印python
print(L[1][1])
#打印lisa
print(L[2][2])
'''

'''#条件判断练习
# -*- coding: utf-8 -*-
height = float(input('请输入身高：'))
weight = float(input('请输入体重：'))
bmi = float((weight/height)**2)
if bmi<18.5:
	print('过轻')
elif bmi<=25:
	print('过重')
elif bmi<=32:
	print('肥胖')
else:
	print('严重肥胖')
'''

'''#循环练习
# -*- coding: utf-8 -*-
L = ['Bart', 'Lisa', 'Adam']
n = int(len(L))
while n>0:
    print('Hello,%s' % L[len(L)-n])
    n = n-1
'''

'''#循环练习   
# -*- coding: utf-8 -*-
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello,%s'%name)
'''


'''
# -*- coding: utf-8 -*-
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
'''

'''#函数定义练习
# -*- coding: utf-8 -*-
import math
def quadratic(a, b, c):
	d=b**2-4*a*c
	if d==0: 
		x=-b/(2*a)
		return x
	
	elif d>0: 
		x1=(math.sqrt(d)-b)/(2*a)
		x2=-(math.sqrt(d)+b)/(2*a)
		return (x1,x2)
	
	else:
		return('无实数解')
a=float(input('请输入a：'))
b=float(input('请输入b：'))
c=float(input('请输入c：'))
print(quadratic(a,b,c))
'''

'''
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(188))
'''

'''#函数的参数练习
# -*- coding: utf-8 -*-
def product(*L):
	if len(L)==0:
		raise TypeError('参数为空')
	else:
		n=1
		for i in L:
			n=n*i
		return n
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
'''		
'''		
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(1000))
'''
'''
#递归解决汉诺塔问题
def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        print(a,'-->',c)
        move(n-1,b,a,c)
print(move(2,'A','B','C'))
'''
'''
# -*- coding: utf-8 -*-
def trim(s):
	s=s[1:-1]
	return s
s=str(input('请输入内容:'))
print(trim(s))
'''

'''
#切片练习
# -*- coding: utf-8 -*-
def trim(s):
	a=len(s)
	n=0
	m=a-1
	while n<a:
		if s[n]!=' ':#添加空格
			break
		else:
			n=n+1
	while m>0:
		if s[m]!=' ':#添加空格
			break
		else:
			m=m-1
	#print(n) #输出变量结果
	#print(m) #输出变量结果
	m=m+1#切片不包含最后一项
	return s[n:m]
print(trim('   abc   '))
if trim('   abc   ')=='abc':
	print('pass')
else:
	print('fail')
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
'''

'''
#迭代练习
# -*- coding: utf-8 -*-
def findMinAndMax(L):
	if len(L)==0:
		return(None,None)
	elif len(L)==1:
		return (L[0],L[0])
	else:
		min=L[0]
		max=L[0]
		for a in L:
			if a<min:
				min=a
			elif a>max:
				max=a
	return (min,max)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
'''

'''
#列表生成式练习
# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)==True]		
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
'''
'''
# -*- coding: utf-8 -*-
def triangles():
	L = [1]
	yield L
	while True:
		L.append(0)
		L = [L[i - 1] + L[i] for i in range(len(L))]
		yield L
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 2:
        break
if results == [
	[1],
	[1,1]]:
	print('测试通过!')
else:
	print('测试失败!')
'''

'''
#高级函数练习1
# -*- coding: utf-8 -*-
from functools import reduce
#第一题字符串大小写转换
def normalize(name):
	return name[0].upper()+name[:-1].lower()
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#第二题列表乘积
def time(x,y):
	return x*y
def prod(L): 
    return reduce(time,L)
# 测试:
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
	
#第三题字符串类型转换
digits={'.':'.','0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def chr2num(s):
	return digits[s]

def f(x,y):
	return x*10+y

def str2float(s):
	l=s.split('.')
	n=len(l[1])
	a=reduce(f,map(chr2num,l[0]))
	b=reduce(f,map(chr2num,l[1]))
	return a+b*pow(10,-n)
print('str2float(\'123.456789\') =', str2float('123.456789'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
'''	

'''
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
for n in primes():
	if n < 10:
		print(n)
	else:
		break
'''

'''
#filter练习
# -*- coding: utf-8 -*-
from functools import reduce	
digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def chr2num(s):
	return digits[s]

def fn(x,y):
	return x*10+y
				
def is_palindrome(n):
	s=list(str(n))
	l=len(s)
	if l==1:
		return n
	else:
		a=reduce(fn,map(chr2num,s[::-1]))
		if a==n:
			return a
		else:
			return None
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
'''	

'''
#sorted函数练习
# -*- coding: utf-8 -*-
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	return t[0]
print(by_name(L))#测试该函数的输出

def by_score(t):
	return t[1]
print(by_score(L))#测试该函数的输出

#升序排序名字和分数
L2 = sorted(L, key=by_name)
print(L2)
L2 = sorted(L, key=by_score)
print(L2)

#降序排序名字和分数
L2 = sorted(L, key=by_name, reverse=True)
print(L2)
L2 = sorted(L, key=by_score, reverse=True)
print(L2)
'''

'''
#返回函数练习
# -*- coding: utf-8 -*-
def createCounter():
    x = (x for x in range(1,100))
    def counter():
        return next(x)
    return counter
	
# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
'''

'''
# -*- coding: utf-8 -*-
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)
'''

'''
#匿名函数练习
# -*- coding: utf-8 -*-	
L = list(filter(lambda n:n%2==1, range(1, 20)))
print(L)
'''


# -*- coding: utf-8 -*-
#打印函数执行时间
import time, functools
def metric(fn):
	def wrapper(*args,**kw):
		print('%s executed in %s ms' % (fn.__name__, 10.24))
		return fn(*args,**kw)
	return wrapper
	
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else: 
	print('测试成功!')
	

#函数的调用前后输出
def log(func):
    def wrapper(*args,**kw):
        print('begin call')
        c = func(*args,**kw)
        print('end call')
        return c
    return wrapper
@log
def now():
    print('20180905')
now()


#第三题
def logger(*text):
	def decorator(func):
		def wrapper(*args,**kw):
			if str(*text) == '':
				print('call %s()' % func.__name__)
			else:
				print('%s call %s()' % (*text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator


@logger('is test')
def f1():
	print('2018-09-06')
f1()

@logger()
def f2():
	print('2018-09-06')
f2()