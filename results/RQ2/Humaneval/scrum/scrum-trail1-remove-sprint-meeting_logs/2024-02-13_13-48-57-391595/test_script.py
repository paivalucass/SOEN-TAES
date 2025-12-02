def unique(l: list):
    # Return sorted unique elements in a list
    # >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    # [0, 2, 3, 5, 9, 123]
    
    # Using set to store unique elements and then converting it to list
    unique_list = list(set(l))
    
    # Sorting the unique elements
    sorted_unique = sorted(unique_list)
    
    # Return the sorted unique elements
    return sorted_unique
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]), [0, 2, 3, 5, 9, 123])

if __name__ == '__main__':
    unittest.main()