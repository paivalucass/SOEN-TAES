def unique_element(arr):
    if not isinstance(arr, list):
        raise TypeError("Input should be a list")
    if len(arr) == 0:
        raise ValueError("List should not be empty")
    if len(set(arr)) == 1:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_Element([1,1,1]), True)

if __name__ == '__main__':
    unittest.main()