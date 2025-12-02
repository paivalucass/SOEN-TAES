def unique_Element(arr):
    if not isinstance(arr, list):
        raise ValueError("Input is not a list")
    if len(arr) < 1:
        return False
    first_element = arr[0]
    for num in arr[1:]:
        if num != first_element:
            return False
    return True

assert unique_Element([1,1,1,1]) == True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_Element([1,1,1]), True)

if __name__ == '__main__':
    unittest.main()