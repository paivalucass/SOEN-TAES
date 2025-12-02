def all_unique(test_list):
    if isinstance(test_list, list):
        return len(test_list) == len(set(test_list))
    else:
        return "Error"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_unique([1,2,3]), True)

if __name__ == '__main__':
    unittest.main()