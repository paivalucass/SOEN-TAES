def choose_num(x, y):
    if x <= 0 or y <= 0:
        return -1

    largest_even = -1
    for num in range(x, y+1):
        if num % 2 == 0:
            if num > largest_even:
                largest_even = num
    
    return largest_even
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(choose_num(12, 15), 14)

    def test2(self):
        self.assertEqual(choose_num(13, 12), -1)

if __name__ == '__main__':
    unittest.main()