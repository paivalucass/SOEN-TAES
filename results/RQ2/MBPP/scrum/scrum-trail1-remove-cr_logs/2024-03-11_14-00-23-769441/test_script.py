def unique_Element(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list")

    if len(arr) == 0 or len(arr) == 1:
        return True

    first_element = arr[0]
    for element in arr:
        if element != first_element:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_Element([1,1,1]), True)

if __name__ == '__main__':
    unittest.main()