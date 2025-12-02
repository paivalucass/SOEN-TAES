def all_unique(test_list):
    if not isinstance(test_list, list):
        raise TypeError("Input must be a list")
    
    unique_elements = set(test_list)
    if len(test_list) == len(unique_elements):
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_unique([1,2,3]), True)

if __name__ == '__main__':
    unittest.main()