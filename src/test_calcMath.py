"""!
* Project Name : Projekt IVS                                                
* File : test_calcMath.py                                                   
* Date : 15.04.2022                                                         
* Last change : 26.04.2022                                                  
* Author : Lukáš Etzler (xetzle00)
* Description : Tests for Math library
"""

import unittest
import calcMath


class TestCalcMath(unittest.TestCase):

    # Testování součtu
    def test_add(self):
        self.assertEqual(calcMath.add(100,5), 105)
        self.assertEqual(calcMath.add(-1,1), 0)
        self.assertEqual(calcMath.add(-1,-125), -126)
        self.assertEqual(calcMath.add(1,-5), -4)
        self.assertEqual(calcMath.add(0,0), 0)

    # Testování rozdílu
    def test_sub(self):
        self.assertEqual(calcMath.sub(100,5), 95)
        self.assertEqual(calcMath.sub(-1,1), -2)
        self.assertEqual(calcMath.sub(-1,-125), 124)
        self.assertEqual(calcMath.sub(1,-5), 6)
        self.assertEqual(calcMath.sub(-1, -1), 0)
        self.assertEqual(calcMath.sub(0, -1), 1)
        self.assertEqual(calcMath.sub(0, 0), 0)

    # Testování násobení
    def test_mul(self):
        self.assertEqual(calcMath.mul(100,5), 500)
        self.assertEqual(calcMath.mul(-1,1), -1)
        self.assertEqual(calcMath.mul(-1,-125), 125)
        self.assertEqual(calcMath.mul(1,-5), -5)
        self.assertEqual(calcMath.mul(-1, -1), 1)
        self.assertEqual(calcMath.mul(0, -1), 0)

    # Testování podílu
    def test_div(self):
        self.assertEqual(calcMath.div(100,5), 20)
        self.assertEqual(calcMath.div(-1,1), -1)
        self.assertEqual(calcMath.div(-1,-125), 0.008)
        self.assertEqual(calcMath.div(1,-5), -0.2)
        self.assertEqual(calcMath.div(-1, -1), 1)
        self.assertEqual(calcMath.div(0, -1), 0)
        self.assertEqual(calcMath.div(0, 1), 0)
        self.assertEqual(calcMath.div(1, 0), "DIVISION BY ZERO")

    # Testování faktoriálu
    def test_factorial(self):
        self.assertEqual(calcMath.factorial(0), 1)
        self.assertEqual(calcMath.factorial(1), 1)
        self.assertEqual(calcMath.factorial(2), 2)
        self.assertEqual(calcMath.factorial(3), 6)
        self.assertEqual(calcMath.factorial(10), 3628800)
        self.assertEqual(calcMath.factorial(25), 15511210043330985984000000)
        self.assertEqual(calcMath.factorial(-1), "NOT POSITIVE NUMBER")
        self.assertEqual(calcMath.factorial(-5), "NOT POSITIVE NUMBER")
        self.assertEqual(calcMath.factorial(-6), "NOT POSITIVE NUMBER")

    # Testování odmocniny
    def test_power(self):
        self.assertEqual(calcMath.power(1,1), 1)
        self.assertEqual(calcMath.power(1,0), 1)
        self.assertEqual(calcMath.power(2,6), 64)
        self.assertEqual(calcMath.power(485,0), 1)
        self.assertEqual(calcMath.power(2,-1), "NOT NATURAL NUMBER")
        self.assertEqual(calcMath.power(2,-5), "NOT NATURAL NUMBER")

    # Testování mocnin
    def test_root(self):
        self.assertEqual(calcMath.root(1,1), 1)
        self.assertEqual(calcMath.root(3,8), 2)
        self.assertEqual(calcMath.root(3,64), 4)
        self.assertEqual(calcMath.root(2,64), 8)
        self.assertEqual(calcMath.root(-2,64), "NUMBER IS NOT POSITIVE NUMBER")
        self.assertEqual(calcMath.root(-2,64), "NUMBER IS NOT POSITIVE NUMBER")
        self.assertEqual(calcMath.root(0,64), "NUMBER IS NOT POSITIVE NUMBER")

    # Testování modula
    def test_mod(self):
        self.assertEqual(calcMath.mod(1,1), 0)  
        self.assertEqual(calcMath.mod(2,1), 0)
        self.assertEqual(calcMath.mod(1,-1), 0)  
        self.assertEqual(calcMath.mod(256,58), 24)  
        self.assertEqual(calcMath.mod(256,-58), -34)  


if __name__ == '__main__':
    unittest.main()

"""*** End of file test_calcMath.py ***"""