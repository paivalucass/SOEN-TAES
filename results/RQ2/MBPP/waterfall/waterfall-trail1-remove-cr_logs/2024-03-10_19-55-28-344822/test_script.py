from typing import List

def remove_elements(main_list: List[int], elements_to_remove: List[int]) -> List[int]:
    result = [element for element in main_list if element not in elements_to_remove]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8]), [1, 3, 5, 7, 9, 10])

if __name__ == '__main__':
    unittest.main()