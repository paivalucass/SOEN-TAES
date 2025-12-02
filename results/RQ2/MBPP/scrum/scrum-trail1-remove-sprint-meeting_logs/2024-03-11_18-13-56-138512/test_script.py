def recursive_list_sum(data_list):
    if not isinstance(data_list, list):
        raise TypeError("Input must be a list")

    total_sum = 0
    for element in data_list:
        if isinstance(element, list):
            total_sum += recursive_list_sum(element)
        elif isinstance(element, (int, float)):
            total_sum += element
        else:
            raise TypeError("Non-numeric value found in the list")

    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(recursive_list_sum([1, 2, [3,4],[5,6]]), 21)

if __name__ == '__main__':
    unittest.main()