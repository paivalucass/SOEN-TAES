def count_list(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input should be a list")

    count = 0
    for item in input_list:
        if isinstance(item, list):
            count += 1
            count += count_list(item)  # recursive call to count sublists
    return count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]), 4)

if __name__ == '__main__':
    unittest.main()