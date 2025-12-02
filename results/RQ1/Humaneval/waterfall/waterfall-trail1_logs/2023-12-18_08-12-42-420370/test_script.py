def sort_even(input_list: list) -> list:
    if len(input_list) <= 1:
        return input_list
    even_indices = [input_list[i] for i in range(len(input_list)) if i % 2 == 0]
    even_indices.sort()
    result = [input_list[i] if i % 2 != 0 else even_indices.pop(0) for i in range(len(input_list))]
    return result
import unittest

class Test(unittest.TestCase):
    def test_sort_even(self):
        self.assertEqual(sort_even([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])

if __name__ == '__main__':
    unittest.main()