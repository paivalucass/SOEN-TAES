def is_octagonal(n):
    if n <= 0:
        return "Error: Invalid Input"

    nth_octagonal_number = n * (3*n - 1)
    return str(nth_octagonal_number)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_octagonal(5), 65)

if __name__ == '__main__':
    unittest.main()