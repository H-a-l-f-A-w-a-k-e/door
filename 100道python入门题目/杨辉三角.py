# 题目 打印出杨辉三角形前十行。
def generate(numRows):
    r = [[1]]
    for i in range(1,numRows):
        r.append(list(map(lambda x,y:x+y, [0]+r[-1],r[-1]+[0])))#构造辅助列表，实现错位相加
    return r[:numRows]
a=generate(10)#输入所需行数
for i in a:
    print(i)