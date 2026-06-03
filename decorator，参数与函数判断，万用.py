import functools
def log(arg=None):
    """
    兼容 @log 和 @log('xxx') 两种用法的装饰器
    :param arg: 可选参数，若为字符串则作为日志前缀；若为函数则是直接装饰的场景
    :return: 装饰后的函数或装饰器工厂
    """
    # 情况1：@log 直接装饰（arg 是被装饰的函数）
    if callable(arg):
        func = arg  # 提取被装饰的函数
        @functools.wraps(func)  # 保留原函数的元信息（如 __name__、__doc__）
        def wrapper(*args, **kwargs):
            print(f"[LOG] 执行函数 {func.__name__}")  # 默认日志逻辑
            return func(*args, **kwargs)  # 执行原函数并返回结果
        return wrapper
    # 情况2：@log('xxx') 带参数装饰（arg 是自定义字符串）
    else:
        prefix = arg  # 提取自定义前缀
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(f"[{prefix}] 执行函数 {func.__name__}")  # 带前缀的日志逻辑
                return func(*args, **kwargs)
            return wrapper
        return decorator
# 测试1：@log 无参数装饰
@log
def test_no_arg():
    print("test_no_arg 内部逻辑")

# 测试2：@log('execute') 带参数装饰
@log('execute')
def test_with_arg():
    print("test_with_arg 内部逻辑")


# 执行测试
test_no_arg()
print("-" * 30)
test_with_arg()