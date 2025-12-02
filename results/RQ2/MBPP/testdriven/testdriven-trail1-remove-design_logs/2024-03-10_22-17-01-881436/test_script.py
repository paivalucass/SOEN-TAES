def geometric_sum(n):
    result = 0
    for i in range(n):
        result += 1 / (pow(2, i))
    return result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(geometric_sum(7), 1.9921875)

if __name__ == '__main__':
    unittest.main()