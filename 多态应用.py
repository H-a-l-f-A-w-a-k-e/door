# 你的类定义写在这里...
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def work(self):
        print("员工正在工作")

    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, bonus):
        super().__init__(name, employee_id)
        self.bonus = bonus
        self.base_salary = base_salary

    def work(self):
        print(f"全职员工 {self.name} 正在处理公司日常事务")

    def calculate_salary(self):
        return self.base_salary + self.bonus


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def work(self):
        print(f"兼职员工 {self.name} 正在完成指定任务")

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Freelancer(Employee):
    def __init__(self, name, employee_id, project_fee):
        super().__init__(name, employee_id)
        self.project_fee = project_fee

    def work(self):
        print(f"自由职业者 {self.name} 正在推进项目进度")

    def calculate_salary(self):
        return self.project_fee


def show_employee_status(employee_list):
    for employee in employee_list:
        employee.work()
        salary = employee.calculate_salary()
        print(f"{employee.name} 的本月薪资为：{salary} 元")


# 创建员工对象
ft_emp = FullTimeEmployee("张三", "E001", 8000, 2000)
pt_emp = PartTimeEmployee("李四", "E002", 50, 80)
freelancer = Freelancer("王五", "E003", 15000)

# 统一展示
employee_list = [ft_emp, pt_emp, freelancer]
show_employee_status(employee_list)