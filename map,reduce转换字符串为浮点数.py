# find the point
# before the point
# behind the point
# plus them
from functools import reduce
def char2num(s):
    digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]
def func(x,y):
    return x*10+y
def func2(x,y):
    return x*0.1+y
def str2float(s):
    # part=s.split('.')
    # s1=part[0]
    # s2=part[1]
    # 后续逻辑需修改
    i=s.find('.')
    s1=s[:i]
    s2=s[:i:-1]
    a=map(char2num,s1)
    b=map(char2num,s2)
    return reduce(func,a)+reduce(func2,b)*0.1


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
