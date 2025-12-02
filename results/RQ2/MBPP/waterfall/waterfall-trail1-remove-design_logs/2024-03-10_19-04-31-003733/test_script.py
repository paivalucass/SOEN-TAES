def recursive_list_sum(data_list):
    cumulative_sum = 0
    if not isinstance(data_list, list):
        raise TypeError("Input must be a list")

    for element in data_list:
        if isinstance(element, list):
            cumulative_sum += recursive_list_sum(element)
        else:
            cumulative_sum += element
    return cumulative_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(recursive_list_sum([1, 2, [3,4],[5,6]]), 21)

if __name__ == '__main__':
    unittest.main()