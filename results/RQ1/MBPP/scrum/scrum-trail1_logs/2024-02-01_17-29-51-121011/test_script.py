def function_under_test(n):
    perrin_numbers = [3, 0, 2]
    result = 0
    for i in range(n):
        result += perrin_numbers[i % 3]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test(9), 49)

if __name__ == '__main__':
    unittest.main()