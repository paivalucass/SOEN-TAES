def recursive_list_sum(data_list):
    if not isinstance(data_list, list):
        raise ValueError("Input is not a list")

    total_sum = 0

    for elem in data_list:
        if isinstance(elem, list):
            total_sum += recursive_list_sum(elem)
        elif isinstance(elem, int):
            total_sum += elem
        else:
            raise ValueError("Error handling for non-numeric elements")

    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(recursive_list_sum([1, 2, [3,4],[5,6]]), 21)

if __name__ == '__main__':
    unittest.main()