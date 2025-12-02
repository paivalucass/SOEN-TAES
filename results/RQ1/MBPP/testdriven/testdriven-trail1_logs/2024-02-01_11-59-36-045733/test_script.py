def power(a, b):
    '''Write a function to calculate the value of 'a' to the power 'b'. '''
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid input"
    if a == 0:
        return 0
    if b == 0:
        return 1
    if a < 0 and not isinstance(b, int):
        return "Invalid input"
    result = 1
    if b > 0:
        for _ in range(b):
            result *= a
    else:
        for _ in range(abs(b)):
            result /= a
    return result
import unittest

class Test(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(3, 4), 81)

if __name__ == '__main__':
    unittest.main()