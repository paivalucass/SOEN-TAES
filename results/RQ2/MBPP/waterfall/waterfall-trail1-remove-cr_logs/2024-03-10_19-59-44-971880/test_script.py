def all_unique(test_list):
    if not isinstance(test_list, list):
        raise ValueError("Input must be a list")

    if len(test_list) != len(set(test_list)):
        return False
    else:
        return True
import unittest

# Function to be tested
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(all_unique([1, 2, 3]), True)

if __name__ == '__main__':
    unittest.main()