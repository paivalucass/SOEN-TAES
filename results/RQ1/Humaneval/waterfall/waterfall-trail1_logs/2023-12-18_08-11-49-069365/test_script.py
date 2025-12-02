def sort_third(l: list) -> list:
    if not l:
        return []
    if any(not isinstance(item, int) for item in l):
        return "Error: Input list contains non-integer elements"

    divisible_by_three = sorted([item for index, item in enumerate(l) if (index+1) % 3 == 0])
    rest_of_elements = [item for index, item in enumerate(l) if (index+1) % 3 != 0]

    sorted_list = rest_of_elements.copy()
    for i in range(len(divisible_by_three)):
        sorted_list.insert((i+1)*3-1, divisible_by_three[i])

    return sorted_list
import unittest

class Test(unittest.TestCase):
    def test_sort_third(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

if __name__ == '__main__':
    unittest.main()