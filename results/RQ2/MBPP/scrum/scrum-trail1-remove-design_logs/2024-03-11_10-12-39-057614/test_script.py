def frequency(a, x):
    count = 0
    for num in a:
        if num == x:
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_frequency(self):
        self.assertEqual(frequency([1, 2, 3], 4), 0)

if __name__ == '__main__':
    unittest.main()