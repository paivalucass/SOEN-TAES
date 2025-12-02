def choose_num(x, y):
    if x <= 0 or y <= 0:
        return -1
    if x > y:
        return -1
    
    largest_even = -1
    for i in range(y, x - 1, -1):
        if i % 2 == 0:
            largest_even = i
            break
    
    return largest_even
import unittest

class Test(unittest.TestCase):
    def test_choose_num(self):
        self.assertEqual(choose_num(12, 15), 14)
        self.assertEqual(choose_num(13, 12), -1)

if __name__ == '__main__':
    unittest.main()