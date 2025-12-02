def is_num_decagonal(n):
    if n < 0:
        return "Error: n must be a positive number"
    elif not isinstance(n, int):
        return "Error: n must be an integer"

    result = n * (7*n - 5)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_num_decagonal(3), 27)

if __name__ == '__main__':
    unittest.main()