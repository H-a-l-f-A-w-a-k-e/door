class Student(object):
    def __init__(self, name, age, grade, score):
        if not isinstance(score, (int, float)):
            raise ValueError('成绩必须是整数或小数')
        if score > 100 or score < 0:
            raise ValueError('成绩必须在0~100之间!')

        self.name = name
        self.age = age
        self.grade = grade
        self.score = score

    def get_score(self):
        if (self.score >= 90):
            return(self.name + '--A')
        elif (self.score >= 80):
            return(self.name + '--B')
        elif (self.score >= 60):
            return(self.name + '--C')
        else:
            return(self.name + '--D')

student1 = Student('Alise', 18, '计算机科学 一年级', 98)

print(student1.get_score())