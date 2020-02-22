# IVS - tests
# Author: Michal Machač, xmacha72
# Date: 21.02.2020

import unittest
import matlib


class test_add(unittest.TestCase):
    def test_add_1(self):
        self.assertEqual(matlib.add(1,1),2)

    def test_add_2(self):
        self.assertEqual(matlib.add(-1,1),0)

    def test_add_3(self):
        self.assertEqual(matlib.add(1,-1),0)

    def test_add_4(self):
        self.assertEqual(matlib.add(-1,-1),-2)

    def test_add_5(self):
        self.assertEqual(matlib.add(0,1),1)

    def test_add_6(self):
        self.assertEqual(matlib.add(1,0),1)

class test_sub(unittest.TestCase):
    def test_sub_1(self):
        self.assertEqual(matlib.sub(1,1),0)

    def test_sub_2(self):
        self.assertEqual(matlib.sub(1,-1),2)

    def test_sub_3(self):
        self.assertEqual(matlib.sub(-1,1),-2)

    def test_sub_4(self):
        self.assertEqual(matlib.sub(-1,-1),0)

    def test_sub_5(self):
        self.assertEqual(matlib.sub(0,1),-1)

    def test_sub_6(self):
        self.assertEqual(matlib.sub(1,0),1)


class test_mul(unittest.TestCase):
    def test_mul_1(self):
        self.assertEqual(matlib.mul(1,1),1)

    def test_mul_2(self):
        self.assertEqual(matlib.mul(1,-1),-1)

    def test_mul_3(self):
        self.assertEqual(matlib.mul(-1,1),-1)

    def test_mul_4(self):
        self.assertEqual(matlib.mul(0,1),0)

    def test_mul_5(self):
        self.assertEqual(matlib.mul(1,0),0)

    def test_mul_6(self):
        self.assertEqual(matlib.mul(5,8),40)

    def test_mul_7(self):
        self.assertEqual(matlib.mul(-8,-5),40)

class test_div(unittest.TestCase):
    def test_div_1(self):
        self.assertEqual(matlib.div(10,2),5)

    def test_div_2(self):
        self.assertEqual(matlib.div(10,-2),-5)

    def test_div_3(self):
        self.assertEqual(matlib.div(1,10),0.1)

    def test_div_4(self):
        self.assertEqual(matlib.div(1,-10),-0.1)

    def test_div_5(self):
        self.assertRaises(ZeroDivisionError, lambda: matlib.div(2, 0))

class test_factorial(unittest.TestCase):
    def test_factorial_1(self):
        self.assertEqual(matlib.factorial(1), 1)

    def test_factorial_2(self):
        self.assertEqual(matlib.factorial(2), 2)

    def test_factorial_3(self):
        self.assertEqual(matlib.factorial(3), 6)

    def test_factorial_4(self):
        self.assertEqual(matlib.factorial(5), 120)

    def test_factorial_5(self):
        self.assertEqual(matlib.factorial(0), 1)

    def test_factorial_6(self):
        self.assertEqual(matlib.factorial(-3), 1)


class test_pow(unittest.TestCase):
    def test_pow_1(self):
        self.assertEqual(matlib.pow(2,1), 2)

    def test_pow_2(self):
        self.assertEqual(matlib.pow(2,2), 4)

    def test_pow_3(self):
        self.assertEqual(matlib.pow(2,3), 8)

    def test_pow_4(self):
        self.assertRaises(ValueError, lambda: matlib.pow(2, -1))

    def test_pow_5(self):
        self.assertRaises(ValueError, lambda: matlib.pow(2, 1.1))

    def test_pow_5(self):
        self.assertEqual(matlib.pow(2,0), 1)


class test_sqrt(unittest.TestCase):
    def test_sqrt_1(self):
        self.assertEqual(matlib.sqrt(8,1), 8)

    def test_sqrt_2(self):
        self.assertEqual(matlib.sqrt(8,3), 2)

    def test_sqrt_3(self):
        self.assertEqual(matlib.sqrt(9,2), 3)

    def test_sqrt_4(self):
        self.assertAlmostEqual(matlib.sqrt(9,3), 2.08008382, places=8)

    def test_sqrt_5(self):
        self.assertRaises(ValueError, lambda: matlib.sqrt(-9,2))

    def test_sqrt_6(self):
        self.assertRaises(ValueError, lambda: matlib.sqrt(9,-2))

class test_modulo(unittest.TestCase):
    def test_modulo_1(self):
        self.assertEqual(matlib.modulo(5,3),2)

    def test_modulo_2(self):
        self.assertRaises(ZeroDivisionError, lambda: matlib.modulo(1,0))

    def test_modulo_3(self):
        self.assertEqual(matlib.modulo(0,3),0)

    def test_modulo_4(self):
        self.assertEqual(matlib.modulo(2,2),0)

if __name__ == '__main__':
    unittest.main()
