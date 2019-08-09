import re
t='UTC+07:00'
n=re.match(r'UTC.(0?)(\d+):',t)
n1=re.match(r'UTC.(0?)(\d+):',t).group(2)
print(n)
print(n1)
