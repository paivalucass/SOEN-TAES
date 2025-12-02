def unique_digits(x):
    if any(num <= 0 for num in x):
        raise ValueError("Input list should only contain positive integers")

    x = sorted(x)

    result = [num for num in x if all(int(digit) % 2 != 0 for digit in str(num))]

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
        self.assertEqual(unique_digits([152, 323, 1422, 10]), [])

if __name__ == '__main__':
    unittest.main()