def min_val(inputList):
    if not inputList:
        raise ValueError("Input list is empty")

    numeric_list = [x for x in inputList if isinstance(x, (int, float))]
    if numeric_list:
        return min(numeric_list)
    else:
        raise ValueError("All elements in the input list are not numeric")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(min_val(['Python', 3, 2, 4, 5, 'version']), 2)

if __name__ == '__main__':
    unittest.main()