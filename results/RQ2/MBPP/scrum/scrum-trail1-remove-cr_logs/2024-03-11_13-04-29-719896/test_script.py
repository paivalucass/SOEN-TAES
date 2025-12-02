def all_unique(test_list):
    if not isinstance(test_list, list):
        raise TypeError("Input should be a list")
    
    unique_set = set(test_list)
    return len(unique_set) == len(test_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_unique([1,2,3]), True)

if __name__ == '__main__':
    unittest.main()