# 题目 暂停一秒输出。
# 程序分析 使用 time 模块的 sleep() 函数。
import time
for i in range(4):
    print(str(int(time.time()))[-2:])
    time.sleep(1)
# 题目 暂停一秒输出，并格式化当前时间。
# 程序分析 同 009.
import time
for i in range(4):
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(1)