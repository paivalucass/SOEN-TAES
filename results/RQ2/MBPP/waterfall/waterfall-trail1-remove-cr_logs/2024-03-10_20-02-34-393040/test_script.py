def median_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1] if a != b != c else a
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_numbers(25,55,65), 55.0)

if __name__ == '__main__':
    unittest.main()