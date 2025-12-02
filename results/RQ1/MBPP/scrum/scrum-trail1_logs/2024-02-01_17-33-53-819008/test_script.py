def difference(n):
    sum_natural = 0
    sum_cubes = 0
    if type(n) != int or n <= 0:
        return "Invalid input"
    elif n > 100000:
        return "Very large value"
    else:
        for i in range(1, n + 1):
            sum_natural += i
            sum_cubes += i ** 3
        return sum_cubes - sum_natural
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(difference(3), 30)

if __name__ == '__main__':
    unittest.main()