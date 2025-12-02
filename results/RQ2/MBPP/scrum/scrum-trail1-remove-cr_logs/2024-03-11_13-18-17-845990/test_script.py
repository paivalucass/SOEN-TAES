def check_greater(arr, number):
    if not arr:
        return False
    assert isinstance(arr, list), "Input 'arr' must be a list"
    assert all(isinstance(x, (int, float)) for x in arr), "All elements in 'arr' must be numbers"
    assert isinstance(number, (int, float)), "Input 'number' must be a number"

    for elem in arr:
        if number <= elem:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test_check_greater(self):
        self.assertEqual(check_greater([1, 2, 3, 4, 5], 4), False)

if __name__ == '__main__':
    unittest.main()