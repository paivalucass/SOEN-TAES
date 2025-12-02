def search(lst) -> int:
    if not lst:
        return -1

    frequency_map = {}
    for num in lst:
        if num > 0:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1

    result = -1
    for num, freq in frequency_map.items():
        if num == freq and num > result:
            result = num

    return result

import unittest

class Test(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search([4, 1, 2, 2, 3, 1]), 2)
        self.assertEqual(search([1, 2, 2, 3, 3, 3, 4, 4, 4]), 3)
        self.assertEqual(search([5, 5, 4, 4, 4]), -1)

if __name__ == '__main__':
    unittest.main()