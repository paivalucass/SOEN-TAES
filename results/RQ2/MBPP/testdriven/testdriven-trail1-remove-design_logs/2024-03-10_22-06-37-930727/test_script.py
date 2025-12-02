def find_Parity(x):
    if not isinstance(x, (int, float)):
        return "Invalid Input"
    
    if x % 2 == 0:
        return False
    else:
        return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Parity(12), False)

if __name__ == '__main__':
    unittest.main()