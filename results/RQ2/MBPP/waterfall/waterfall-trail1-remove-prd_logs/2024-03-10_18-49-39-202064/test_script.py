def count_list(input_list):
    if not isinstance(input_list, list) or any(not isinstance(sublist, list) for sublist in input_list):
        raise TypeError("Input is not a list of lists")
    
    return len(input_list)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]), 4)

if __name__ == '__main__':
    unittest.main()