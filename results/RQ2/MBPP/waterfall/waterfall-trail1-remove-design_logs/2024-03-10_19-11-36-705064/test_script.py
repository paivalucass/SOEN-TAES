def count_first_elements(test_tup):
    try:
        return test_tup.index((4, 6))
    except ValueError:
        return len(test_tup)
import unittest

class Test(unittest.TestCase):
    def test_count_first_elements(self):
        self.assertEqual(count_first_elements((1, 5, 7, (4, 6), 10)), 3)

if __name__ == '__main__':
    unittest.main()