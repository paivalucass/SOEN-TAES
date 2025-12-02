def all_unique(test_list):
    return len(test_list) == len(set(test_list))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_unique([1,2,3]), True)

if __name__ == '__main__':
    unittest.main()