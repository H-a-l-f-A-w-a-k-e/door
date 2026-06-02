"""基础装饰器：打印函数调用前后的日志"""

def log_call(func):
    def wrapper(*args, **kwargs):  # 兼容任意参数
        print('begin call')
        result = func(*args, **kwargs)  # 执行原函数
        print('end call')
        return result  # 返回原函数的结果
    return wrapper

# 测试
@log_call
def greet(name):
    print(f"Hello, {name}!")
    return "Greeting done"

greet("Alice")
# 输出：
# begin call
# Hello, Alice!
# end call