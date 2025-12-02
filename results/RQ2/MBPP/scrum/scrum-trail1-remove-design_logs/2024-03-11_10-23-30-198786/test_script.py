def count_first_elements(test_tup):
    count = 0
    for item in test_tup:
        if isinstance(item, tuple):
            break
        count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_first_elements((1, 5, 7, (4, 6), 10)), 3)

if __name__ == '__main__':
    unittest.main()