if __name__ == '__main__':
    n = int(input('请输入总人数:'))
    num = []
    for i in range(n):
        num.append(i + 1)
    i = 0#索引
    k = 0#计数器
    m = 0#已出列人数
    while m < n - 1:
        if num[i] != 0 : k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 1
        i += 1
        if i == n : i = 0#循环引（索引超出范围时，重置为0开始）
    i = 0
    while num[i] == 0: i += 1#找出最后一个人的索引
    print(num[i])