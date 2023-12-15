import unittest
from employee1 import Employee


class TestEmployee(unittest.TestCase):


    def test_email(self):
        print('test_email')
        emp_1 = Employee('hari', 'thushan', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)
        
        self.assertEqual(emp_1.email, 'hari.thushan@email.com')
        self.assertEqual(emp_2.email, 'Sue.Smith@email.com')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.email, 'John.thushan@email.com')
        self.assertEqual(emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        print('test_fullname')
        emp_1 = Employee('hari', 'thushan', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)
        
        self.assertEqual(emp_1.fullname, 'hari thushan')
        self.assertEqual(emp_2.fullname, 'Sue Smith')

        emp_1.first = 'John'
        emp_2.first = 'Jane'

        self.assertEqual(emp_1.fullname, 'John thushan')
        self.assertEqual(emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test_apply_raise')
        emp_1 = Employee('hari', 'thushan', 50000)
        emp_2 = Employee('Sue', 'Smith', 60000)
        
        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 52500)
        self.assertEqual(emp_2.pay, 63000)


if __name__ == '__main__':
    unittest.main()