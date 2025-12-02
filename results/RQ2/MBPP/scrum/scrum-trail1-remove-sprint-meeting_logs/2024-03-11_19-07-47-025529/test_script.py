def unique_Element(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    for num in arr:
        if not isinstance(num, (int, float)):
            raise ValueError("List must contain only numeric values")
    if len(set(arr)) == 1:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test_unique_Element(self):
        self.assertEqual(unique_Element([1,1,1]), True)

if __name__ == '__main__':
    unittest.main()