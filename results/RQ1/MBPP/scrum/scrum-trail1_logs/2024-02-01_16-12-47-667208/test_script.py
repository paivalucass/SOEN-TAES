def perfect_squares(a, b):
    result = []
    if not isinstance(a, int) or not isinstance(b, int) or a > b:
        return "Invalid Input"
    for num in range(a, b+1):
        if (num**0.5).is_integer():
            result.append(num)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(perfect_squares(1, 30), [1, 4, 9, 16, 25])

if __name__ == '__main__':
    unittest.main()