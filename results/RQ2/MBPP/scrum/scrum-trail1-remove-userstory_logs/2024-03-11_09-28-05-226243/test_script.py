def find_combinations(test_list):
    result = []
    for i in range(len(test_list)):
        for j in range(i+1, len(test_list)):
            sum_tuple = (test_list[i][0] + test_list[j][0], test_list[i][1] + test_list[j][1])
            result.append(sum_tuple)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]), [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)])

if __name__ == '__main__':
    unittest.main()