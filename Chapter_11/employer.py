

class Employee():
    '''This class store basic employee info and also gives raise to them'''

    def __init__(self, first_name, last_name, current_salary, salary_raise=5000):
        self.first_name = first_name
        self.last_name = last_name
        self.current_salary = current_salary
        self.salary_raise = salary_raise
        self.info = {}

    def first_last_name_salary(self):
        self.info['First_Name'] = self.first_name
        self.info['Last_Name'] = self.last_name
        self.info['Current_Annual_Salary'] = self.current_salary
        return self.info

    def give_raise(self, salary_raise):
        print(f"Congracts you got {salary_raise}$ salary raise! ")
        self.current_salary += salary_raise
        return salary_raise


employee_1 = Employee("Hamza", "Ansari", 6500)
print(employee_1.first_last_name_salary())
employee_1.give_raise(4000)
print(employee_1.first_last_name_salary())
