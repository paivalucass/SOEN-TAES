def check_value(d, n):
    if not isinstance(d, dict) or not isinstance(n, int):
        raise TypeError("Input parameters must be a dictionary and an integer")
    
    if n == 0:
        return False
    
    if len(set(d.values())) == 1 and n != 0:
        return True
    
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_value({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}, 10), False)

if __name__ == '__main__':
    unittest.main()