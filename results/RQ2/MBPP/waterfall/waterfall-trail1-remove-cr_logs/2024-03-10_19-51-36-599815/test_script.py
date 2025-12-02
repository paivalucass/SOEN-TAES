def is_Diff(n):
    if type(n) != int or n is None:
        raise ValueError("Invalid input. Please provide a non-null integer.")

    return n % 11 == 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Diff(12345), False)

if __name__ == '__main__':
    unittest.main()