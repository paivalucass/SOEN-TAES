def sequential_search(dlist, item):
    if not isinstance(dlist, list) or len(dlist) == 0:
        raise ValueError("Invalid input: dlist must be a non-empty list")

    if not isinstance(item, (int, float, str)):
        raise ValueError("Invalid input: item must be a valid data type (int, float, or str)")

    for index, element in enumerate(dlist):
        if element == item:
            return (True, index)
    return (False, -1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequential_search([11,23,58,31,56,77,43,12,65,19], 31), (True, 3))

if __name__ == '__main__':
    unittest.main()