def recursive_list_sum(data_list):
    if not isinstance(data_list, list):
        return "Invalid input"
    total_sum = 0
    for item in data_list:
        if isinstance(item, list):
            total_sum += recursive_list_sum(item)
        elif isinstance(item, int):
            total_sum += item
        else:
            return "Invalid input"
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(recursive_list_sum([1, 2, [3, 4], [5, 6]]), 21)

if __name__ == '__main__':
    unittest.main()