def find_Parity(x):
    if x % 2 == 0:
        return False  # Even parity
    else:
        return True   # Odd parity
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Parity(12), False)

if __name__ == '__main__':
    unittest.main()