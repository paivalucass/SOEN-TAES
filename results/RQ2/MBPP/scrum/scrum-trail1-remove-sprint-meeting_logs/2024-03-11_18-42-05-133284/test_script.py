def min_val(listval):
    if not listval:
        raise ValueError("Input list is empty")

    min_value = None

    for element in listval:
        if isinstance(element, (int, float)):
            if min_value is None or element < min_value:
                min_value = element

    if min_value is None:
        raise ValueError("No numeric value found in the list")

    return min_value
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_val(['Python', 3, 2, 4, 5, 'version']), 2)

if __name__ == '__main__':
    unittest.main()