def count_list(input_list):
    if not isinstance(input_list, list):
        raise ValueError("Input is not a list")

    count = sum(isinstance(item, list) for item in input_list)
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]), 4)

if __name__ == '__main__':
    unittest.main()