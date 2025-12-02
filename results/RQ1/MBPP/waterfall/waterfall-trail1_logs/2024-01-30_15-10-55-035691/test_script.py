def find_combinations(test_list):
    if not test_list:
        return []
    res = {(test_list[i][0] + test_list[j][0], test_list[i][1] + test_list[j][1]) for i in range(len(test_list)) for j in range(len(test_list))}
    return list(res)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]), [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)])

if __name__ == '__main__':
    unittest.main()