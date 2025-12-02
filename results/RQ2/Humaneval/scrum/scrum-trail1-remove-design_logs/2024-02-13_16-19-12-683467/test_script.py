def odd_count(lst):
    result = []
    for s in lst:
        count = sum(1 for c in s if int(c) % 2 != 0)
        result.append('the number of odd elements {}n the str{}ng {} of the {}nput.'.format(count, count, count, count))
    return result
import unittest

class Test(unittest.TestCase):
    def test_odd_count(self):
        self.assertEqual(function_under_test(['1234567']), ["the number of odd elements 4n the str1234567ng 1234567 of the 1234567nput."])
        self.assertEqual(function_under_test(['3', '11111111']), ["the number of odd elements 1n the str3ng 3 of the 3nput.", "the number of odd elements 8n the str11111111ng 11111111 of the 11111111nput."])

if __name__ == '__main__':
    unittest.main()