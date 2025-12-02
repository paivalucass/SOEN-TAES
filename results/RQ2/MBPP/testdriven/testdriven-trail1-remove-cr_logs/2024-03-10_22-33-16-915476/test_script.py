def frequency(a, x):
    count = 0
    if not isinstance(x, list):
        return 0
    for num in x:
        if num == a:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency([1, 2, 3], 4), 0)

if __name__ == '__main__':
    unittest.main()