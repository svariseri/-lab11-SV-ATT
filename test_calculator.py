import unittest
from calculator import *
#https://github.com/svariseri/-lab11-SV-ATT.git
#Partner 1: Sreesha Variseri
#Partner 2: An Tuan Tran

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
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
        self.assertEqual(div(3,-9), -3)
        self.assertEqual(div(3, 9), 3)
        self.assertEqual(div(-3, -9), 3)
        self.assertEqual(div(-3, 9), -3)

    ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0,5)
        self.assertEqual(log(2,8),3)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertEqual(hypotenuse(-3, 4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)
    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-1)

    #     #    square_root(NUM)
        self.assertEqual(square_root(4),2)
    #     # Test basic function
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()