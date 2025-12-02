def all_unique(test_list):
    if not isinstance(test_list, list) or len(test_list) == 0:
        raise ValueError("Input must be a non-empty list")

    unique_elements = set(test_list)

    return len(unique_elements) == len(test_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_unique([1,2,3]), True)

if __name__ == '__main__':
    unittest.main()