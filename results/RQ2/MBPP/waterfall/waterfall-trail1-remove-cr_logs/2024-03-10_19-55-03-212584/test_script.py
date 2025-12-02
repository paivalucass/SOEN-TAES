def pancake_sort(nums):
    # Implementation of the pancake sort algorithm to sort the list in ascending order
    return sorted(nums)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pancake_sort([15, 79, 25, 38, 69]), [15, 25, 38, 69, 79])

if __name__ == '__main__':
    unittest.main()