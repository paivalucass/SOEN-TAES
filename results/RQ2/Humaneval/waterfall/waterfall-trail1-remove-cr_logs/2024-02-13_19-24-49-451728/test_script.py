def choose_num(x, y):
    if x <= 0 or y <= 0:
        return "Error: x and y must be positive integers"
    if x % 2 != 0:
        x += 1
    if y % 2 != 0:
        y -= 1
    if x > y:
        return -1
    return y
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(choose_num(12, 15), 14)
    
    def test2(self):
        self.assertEqual(choose_num(13, 12), -1)

if __name__ == '__main__':
    unittest.main()