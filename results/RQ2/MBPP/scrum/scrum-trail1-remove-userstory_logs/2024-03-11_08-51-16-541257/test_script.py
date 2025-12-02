def smallest_num(xs):
    if not xs:
        return None
    
    min_num = min(xs)
    return min_num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(smallest_num([10, 20, 1, 45, 99]), 1)

if __name__ == '__main__':
    unittest.main()