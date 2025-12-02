def catalan_number(num):
    if not isinstance(num, int) or num <= 0:
        return 0
    
    catalan_number = 1
    for i in range(0, num):
        catalan_number = catalan_number * 2 * (2 * i + 1) / (i + 2)
    
    return int(catalan_number)
import unittest

class Test(unittest.TestCase):
    def test_catalan_number(self):
        self.assertEqual(catalan_number(10), 16796)

if __name__ == '__main__':
    unittest.main()