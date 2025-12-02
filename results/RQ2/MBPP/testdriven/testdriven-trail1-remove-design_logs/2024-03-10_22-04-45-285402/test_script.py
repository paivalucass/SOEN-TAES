def max_val(listval):
    # Type check for input parameter listval to ensure it is a list
    if not isinstance(listval, list):
        raise TypeError("Input parameter listval must be a list")

    # Remove non-numeric values from the list
    numeric_list = [x for x in listval if isinstance(x, (int, float))]

    # Check if the numeric_list is empty
    if len(numeric_list) == 0:
        raise ValueError("EmptyListError")

    # Find the maximum value in the numeric_list
    max_value = max(numeric_list)

    return max_value
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_val(['Python', 3, 2, 4, 5, 'version']), 5)

if __name__ == '__main__':
    unittest.main()