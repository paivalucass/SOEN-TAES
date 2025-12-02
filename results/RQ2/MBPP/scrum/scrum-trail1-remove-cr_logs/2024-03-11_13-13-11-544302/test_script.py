def find_Parity(x): 
    if x % 2 != 0:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Parity(12), False)

if __name__ == '__main__':
    unittest.main()