# 题目 有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
from collections import *
li=[1,2,3,4,5,6,7,8,9]
deq=deque(li,maxlen=len(li))
print(li)
deq.rotate(int(input('rotate:')))
print(list(deq))
# 优点：代码极简（核心只有一行）、语义清晰（rotate 顾名思义）、执行效率高（底层 C 语言实现的双向链表操作）。
# 适用场景：不仅适用于这道题，还广泛应用于缓冲区管理、最近最少使用缓存等需要循环移动数据的算法场景中。