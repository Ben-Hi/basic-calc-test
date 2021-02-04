import unittest
import calculator

class Test_TestCalculator(unittest.TestCase):
    # Add Method testing
    def test_add_pos(self):
        result = calculator.calc_add(1,1)
        self.assertEqual(result, 2)

    def test_add_pos_neg(self):
        result = calculator.calc_add(2,-1)
        self.assertEqual(result, 1)

    def test_add_int_float(self):
        self.assertEqual((calculator.calc_add(1,0.5)),1.5)

    def test_add_int_string(self):
        with self.assertRaises(TypeError):
            calculator.calc_add(1, "string")

    # Sub Method testing
    def test_sub_pos(self):
        self.assertEqual((calculator.calc_sub(1,1)),0)

    def test_sub_pos_neg(self):
        self.assertEqual((calculator.calc_sub(1,-1)),2)

    def test_sub_int_float(self):
        self.assertEqual((calculator.calc_sub(1,0.5)),0.5)

    def test_sub_int_string(self):
        with self.assertRaises(TypeError):
            calculator.calc_sub(1, "string")
    
    # Mul Method testing
    def test_mul_pos(self):
        self.assertEqual(calculator.calc_mul(5,2),10)

    def test_mul_pos_neg(self):
        self.assertEqual(calculator.calc_mul(5,-2),-10)

    def test_mul_int_float(self):
        self.assertEqual(calculator.calc_mul(10,1.5), 15)

    def test_mul_int_string(self):
        self.assertEqual(calculator.calc_mul(2,"string"),"stringstring")

    # Div Method testing
    def test_div_pos(self):
        self.assertEqual(calculator.calc_div(10,2), 5)

    def test_div_pos_neg(self):
        self.assertEqual(calculator.calc_div(10,-2), -5)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.calc_div(1,0)

    def test_div_int_float(self):
        self.assertEqual(calculator.calc_div(10,0.5), 20)

    def test_div_int_string(self):
        with self.assertRaises(TypeError):
            calculator.calc_div(10, "string")

if __name__ == '__main__':
    unittest.main()