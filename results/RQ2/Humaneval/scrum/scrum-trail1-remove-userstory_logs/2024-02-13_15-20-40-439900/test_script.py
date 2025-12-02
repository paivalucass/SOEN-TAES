def odd_count(lst):
    result = []
    for string in lst:
        odd_count = sum(1 for char in string if int(char) % 2 != 0)
        result.append('the number of odd elements {}n the str{}ng {} of the {}nput.'.format(odd_count, str(odd_count), str(string), str(string)))
    return result
import unittest

class Test(unittest.TestCase):
    def test_odd_count(self):
        self.assertEqual(odd_count(['1234567']), ["the number of odd elements 4n the str4ng 4 of the 4nput."])
        self.assertEqual(odd_count(['3', '11111111']), ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."])

if __name__ == '__main__':
    unittest.main()