def count_list(input_list):
    count = 0
    for sublist in input_list:
        if isinstance(sublist, list):
            count += 1
        else:
            return "Error: Non-list element found"
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]), 4)

if __name__ == '__main__':
    unittest.main()