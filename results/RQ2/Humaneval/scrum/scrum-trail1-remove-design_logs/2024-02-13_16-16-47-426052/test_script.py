def unique_digits(x):
    result = []
    for num in x:
        digits = [int(d) for d in str(num)]
        if all(digit % 2 != 0 for digit in digits):
            result.append(num)
    return sorted(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(function_under_test([152, 323, 1422, 10]), [])

if __name__ == '__main__':
    unittest.main()