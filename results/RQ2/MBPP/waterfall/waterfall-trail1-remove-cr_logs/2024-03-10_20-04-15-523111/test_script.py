def count_element_in_list(list1, x):
    if not list1:
        return 0  
    count = 0
    for sublist in list1:
        if isinstance(sublist, list) and x in sublist: 
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_element_in_list(self):
        self.assertEqual(count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1), 3)

if __name__ == '__main__':
    unittest.main()