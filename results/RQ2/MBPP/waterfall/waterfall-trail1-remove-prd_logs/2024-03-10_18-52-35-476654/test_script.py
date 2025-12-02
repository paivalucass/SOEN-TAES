def find_sum(arr):
    try:
        if not arr:
            raise ValueError("Input list is empty")

        for element in arr:
            if not isinstance(element, (int, float)):
                raise ValueError("Non-numeric value found in the input list")

        unique_elements = set(arr)
        sum_of_unique_elements = sum(unique_elements)

        return sum_of_unique_elements

    except ValueError as ve:
        return str(ve)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_sum([1,2,3,1,1,4,5,6]), 21)

if __name__ == '__main__':
    unittest.main()