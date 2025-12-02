def smallest_num(xs):
    if not xs:
        return "Error: Empty list input"
    
    min_num = xs[0]
    for num in xs:
        if num < min_num:
            min_num = num
    
    return min_num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(smallest_num([10, 20, 1, 45, 99]), 1)

if __name__ == '__main__':
    unittest.main()