def count_list(input_list):
    count = 0
    for element in input_list:
        if isinstance(element, list):
            count += 1
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]), 4)

if __name__ == '__main__':
    unittest.main()