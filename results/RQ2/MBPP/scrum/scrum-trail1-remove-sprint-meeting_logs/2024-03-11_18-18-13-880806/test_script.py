def frequency_lists(lists):
    frequency_map = {}
    for sublist in lists:
        for item in sublist:
            if item in frequency_map:
                frequency_map[item] += 1
            else:
                frequency_map[item] = 1
    return frequency_map
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]), {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1})

if __name__ == '__main__':
    unittest.main()