def return_sum(dict):
    sum = 0
    for value in dict.values():
        sum += value
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(return_sum({'a': 100, 'b':200, 'c':300}), 600)

if __name__ == '__main__':
    unittest.main()