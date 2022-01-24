import unittest
from employer import Employee


class test_Employee(unittest.TestCase):
    '''This test will varify the default and custom raise for the customers'''

    def setUp(self):
        self.employee = Employee("Hamza", "Ansari", 7500)
        self.hike = [2000]

    def test_Salary_Raise(self):
        first = self.employee.give_raise(self.hike[0])
        self.assertEquals(first, 2000)
        second = self.employee.give_raise(self.salary_raise)
        self.assertEquals(second, 5000)


if __name__ == '__main__':
    unittest.main()
