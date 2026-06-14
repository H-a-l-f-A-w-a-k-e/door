#手动
# def int2(x,base=2):
#     return int(x,base)
#自动
import functools
int2 = functools.partial(int, base=2)     #设置默认值