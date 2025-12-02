def search(lst):
    if not lst or not all(isinstance(x, int) and x > 0 for x in lst):
        raise ValueError("Input list must be non-empty and contain only positive integers")

    freq_dict = {}
    result = -1

    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
        
        if freq_dict[num] >= num:
            result = max(result, num)

    return result
import unittest

class Test(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

if __name__ == '__main__':
    unittest.main()