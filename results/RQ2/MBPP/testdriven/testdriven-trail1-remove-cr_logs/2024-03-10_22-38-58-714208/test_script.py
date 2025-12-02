def check_distinct(test_tup):
    elements_set = set()
    for element in test_tup:
        if element in elements_set:
            return False
        elements_set.add(element)
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_distinct((1, 4, 5, 6, 1, 4)), False)

if __name__ == '__main__':
    unittest.main()