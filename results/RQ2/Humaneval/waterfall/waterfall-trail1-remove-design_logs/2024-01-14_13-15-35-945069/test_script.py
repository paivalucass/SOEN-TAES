def unique_digits(x):
    unique_digits_list = []
    for num in x:
        if all(int(digit) % 2 != 0 for digit in str(num)):
            unique_digits_list.append(num)

    return sorted(unique_digits_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(function_under_test([152, 323, 1422, 10]), [])

if __name__ == '__main__':
    unittest.main()