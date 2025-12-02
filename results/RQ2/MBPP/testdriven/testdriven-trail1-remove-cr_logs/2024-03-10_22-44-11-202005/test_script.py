def difference(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    try:
        sum_of_numbers = sum(range(1, n+1))
        sum_of_cubes = sum(i**3 for i in range(1, n+1))
        return sum_of_cubes - sum_of_numbers
    except Exception as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(difference(3), 30)

if __name__ == '__main__':
    unittest.main()