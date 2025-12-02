def find_Parity(x): 
    try:
        if isinstance(x, int):
            return x % 2 != 0
        else:
            return 'Error'
    except TypeError:
        return 'Error'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Parity(12), True)

if __name__ == '__main__':
    unittest.main()