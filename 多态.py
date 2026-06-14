class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "汪汪汪!"

class Cat(Animal):
    def speak(self):
        return "喵喵喵!"

class Duck(Animal):
    def speak(self):
        return "嘎嘎嘎!"

# 多态：同一个函数，接收不同的对象，表现不同
# def make_speak(animal):
#     print(animal.speak())
def make_speak(obj):
    print(obj.speak())
# 使用
dog = Dog()
cat = Cat()
duck = Duck()

make_speak(dog)   # 汪汪汪!
make_speak(cat)   # 喵喵喵!
make_speak(duck)  # 嘎嘎嘎!



# 不需要继承 Animal，只要有 speak() 方法就行！
class Robot:
    def speak(self):
        return "嗡嗡嗡! 我是机器人!"

class Car:
    def speak(self):
        return "滴滴滴! 我是汽车!"

# 同样的函数
# def make_speak(obj):
#     print(obj.speak())

# 使用
robot = Robot()
car = Car()

make_speak(robot)  # 嗡嗡嗡! 我是机器人!
make_speak(car)    # 滴滴滴! 我是汽车!