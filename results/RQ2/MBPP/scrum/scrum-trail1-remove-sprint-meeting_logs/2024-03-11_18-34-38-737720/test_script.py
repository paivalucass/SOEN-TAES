def all_unique(test_list):
    unique_set = set()
    for element in test_list:
        if element in unique_set:
            return False
        unique_set.add(element)
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_unique([1,2,3]), True)

if __name__ == '__main__':
    unittest.main()