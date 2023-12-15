import unittest
import calc

# # sample test
# class TestCalc(unittest.TestCase):
    
#     def test_add(self):
#         result = calc.add(5, 10)
#         self.assertEqual(result, 15)


# we need to create a class that inherits from unittest.TestCase
class TestCalc(unittest.TestCase):
    # it's neccessary that the naming convention of the testing methods should be start with "test"
    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)
        
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5),5)
        self.assertEqual(calc.subtract(-1,1),-2)
        self.assertEqual(calc.subtract(-1,-1),0)
        
    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-1,1),-1)
        self.assertEqual(calc.multiply(-1,-1),1)
        
    def test_divide(self):
        self.assertEqual(calc.divide(10,5),2)
        self.assertEqual(calc.divide(-1,1),-1)
        self.assertEqual(calc.divide(-1,-1),1)
        self.assertEqual(calc.divide(5,2),2.5)
        
        # this test throws the value error, hence the test doesn't fail
        self.assertRaises(ValueError, calc.divide, 10, 0)
        
        # another way using context manager
        with self.assertRaises(ValueError):
            calc.divide(10,0)
        
        
        # this test throws the value error, hence the test  fails
        self.assertRaises(ValueError, calc.divide, 10, 2)
        

## "python -m unittest test_calc.py" 

# run using "python test_calc.py" if the  if the main() function is initialized like this
if __name__ == '__main__':
    unittest.main()