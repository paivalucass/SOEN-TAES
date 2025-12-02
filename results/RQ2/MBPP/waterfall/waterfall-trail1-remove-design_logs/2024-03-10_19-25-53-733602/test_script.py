def odd_num_sum(n) :
    result = 0
    for i in range(1, 2*n+1, 2):
        result += i**4
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_num_sum(2), 82)

if __name__ == '__main__':
    unittest.main()