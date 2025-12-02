def median_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    if numbers[0] == numbers[1] and numbers[1] == numbers[2]:
        return numbers[0]
    else:
        return numbers[1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_numbers(25, 55, 65), 55.0)

if __name__ == '__main__':
    unittest.main()