# way1
# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#         return True
# way2埃氏筛法（filter）
# def odd_iter():#先生成一个奇数数列
#     n=1
#     while True:
#         n+=2
#         yield n
# def not_divisible(n):#筛选
#     return lambda x: x%n>0
# def primes():
#     yield 2
#     it =odd_iter()
#     while True:
#         n=next(it)
#         yield n
#         it = filter(not_divisible(n),it)
# for n in primes():
#     if n<100:#可调整所需素数范围
#         print(n)
#     else:
#         break
# way3埃氏筛法
# def prime_generator():
#     n=2
#     while True:
#         is_prime=True
#         for i in range(2,int(n**0.5)+1):
#             if n%i ==0:
#                 is_prime=False
#                 break
#         if is_prime:
#             yield n
#         n+=1
# gen=prime_generator()
# for _ in range(10):#控制数量
#     print(next(gen),end=' ')
#pythonic单行写法(只用于判断） 
is_prime=lambda n:n>1 and all(n%i !=0 for i in range(2,int(n**0.5)+1))
print(is_prime(41))