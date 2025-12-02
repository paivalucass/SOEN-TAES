def find_Parity(x):
    if not isinstance(x, int) or x < 0:
        return "Error: Input is not a valid positive integer"
    
    is_odd_parity = x % 2 != 0
    return is_odd_parity
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Parity(12), False)

if __name__ == '__main__':
    unittest.main()