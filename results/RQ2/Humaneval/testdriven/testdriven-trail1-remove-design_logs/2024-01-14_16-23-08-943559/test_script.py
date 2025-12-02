def multiply(first_integer, second_integer):
    result = int(str(abs(first_integer))[-1]) * int(str(abs(second_integer))[-1])
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)
        self.assertEqual(multiply(14,-15), 20)

if __name__ == '__main__':
    unittest.main()