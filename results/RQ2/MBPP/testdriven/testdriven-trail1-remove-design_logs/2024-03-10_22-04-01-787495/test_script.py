def is_num_decagonal(n):
    if n < 1:
        return "Invalid input"
    else:
        decagonal_number = n * (9 * n - 7)
        return decagonal_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_num_decagonal(3), 27)

if __name__ == '__main__':
    unittest.main()