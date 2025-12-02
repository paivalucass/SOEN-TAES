def find_combinations(test_list):
    result = []
    for idx, tpl in enumerate(test_list):
        for tpl2 in test_list[idx+1:]:
            result.append((tpl[0] + tpl2[0], tpl[1] + tpl2[1]))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]), [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)])

if __name__ == '__main__':
    unittest.main()