import unittest
from calculator import *
#https://github.com/svariseri/-lab11-SV-ATT.git
#Partner 1: Sreesha Variseri
#Partner 2: An Tuan Tran

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertAlmostEqual(add(1.1, 2), 3.1)
        self.assertEqual(add(0, 3), 3)
        self.assertEqual(add(-1,1), 0)

        # 3 assertions
    #     fill in code


    def test_subtract(self):
        self.assertEqual(sub(1,1), 0)# 3 assertions
        self.assertAlmostEqual(sub(1.1, 1), 0.1)
        self.assertEqual(sub(1, -1), 2)
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(-3,3),-9)
        self.assertEqual(mul(3,3),9)
        self.assertEqual(mul(-3, -3), 9)
        self.assertEqual(mul(100,100),10000)
        self.assertEqual(mul(10000,0),0)

    def test_divide(self): # 3 assertions
        self.assertFalse(div(0,1))
        self.assertEqual(div(9,-3), -3)
        self.assertEqual(div(9, 3), 3)
        self.assertEqual(div(-9, -3), 3)
        self.assertEqual(div(-9, 3), -3)

    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    #     fill in code

    def test_logarithm(self): # 3 assertions

        self.assertEqual(log(10, 10), 1)
        self.assertAlmostEqual(log(100, 10), 2)
        self.assertEqual(log(4, 2), 2)


    #     fill in code

    def test_log_invalid_base(self): # 1 assertion
        with self. assertRaises(ZeroDivisionError):
            log(10, 1)
        with self.assertRaises(ValueError):
            log(1, 0)
        with self.assertRaises(ValueError):
            log(1, -1)
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(-3, 4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)
    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()