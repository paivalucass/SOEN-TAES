def frequency(a, x):
    if not a:
        return "Input list 'a' is empty"
    
    count = a.count(x)
    return count if x in a else 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency([1,2,3], 4), 0)

if __name__ == '__main__':
    unittest.main()