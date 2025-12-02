def add(lst):
    total = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            total += lst[i]
    return total
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add([4, 2, 6, 7]), 2)

if __name__ == '__main__':
    unittest.main()