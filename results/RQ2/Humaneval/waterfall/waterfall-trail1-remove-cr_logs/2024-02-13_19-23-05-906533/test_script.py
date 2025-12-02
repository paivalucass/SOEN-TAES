def add(lst):
    sum = 0
    for i in range(len(lst)):
        if i % 2 != 0 and lst[i] % 2 == 0:
            sum += lst[i]
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

if __name__ == '__main__':
    unittest.main()