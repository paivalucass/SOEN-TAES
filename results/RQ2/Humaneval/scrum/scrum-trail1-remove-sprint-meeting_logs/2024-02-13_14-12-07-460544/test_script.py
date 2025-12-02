def multiply(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return "Error: Both parameters should be integers."
    a_str = str(a)
    b_str = str(b)
    a_unit = int(a_str[-1])
    b_unit = int(b_str[-1])
    product = a_unit * b_unit
    return product
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)
        self.assertEqual(multiply(14, -15), 20)

if __name__ == '__main__':
    unittest.main()