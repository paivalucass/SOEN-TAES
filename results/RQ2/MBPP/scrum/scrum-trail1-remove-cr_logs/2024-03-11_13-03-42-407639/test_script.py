def count_first_elements(test_tup):
    count = 0
    for item in test_tup:
        if item == (4, 6):
            return count
        count += 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_first_elements((1, 5, 7, (4, 6), 10)), 3)

if __name__ == '__main__':
    unittest.main()