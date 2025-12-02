def cumulative_sum(test_list):
    result = []
    for tpl in test_list:
        cumulative_sum = 0
        for num in tpl:
            cumulative_sum += num
        result.append(cumulative_sum)
    return sum(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cummulative_sum([(1, 3), (5, 6, 7), (2, 6)]), 30)

if __name__ == '__main__':
    unittest.main()