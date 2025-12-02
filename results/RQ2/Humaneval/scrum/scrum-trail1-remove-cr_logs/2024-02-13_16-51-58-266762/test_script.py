def unique(l: list):
    if not isinstance(l, list):
        raise ValueError("Input should be a list")
    if len(l) == 0:
        return []
    
    unique_list = sorted(set(l))  # remove duplicates and sort the list
    return unique_list
import unittest

class Test(unittest.TestCase):
    def test_unique(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

if __name__ == '__main__':
    unittest.main()