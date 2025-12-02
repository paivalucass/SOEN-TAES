def odd_num_sum(n):
    if type(n) != int:
        return "Error: Invalid input"
    if n <= 0:
        return 0
    else:
        total = 0
        for i in range(1, 2*n, 2):
            total += i**4
        return total
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(odd_num_sum(2), 82)

if __name__ == '__main__':
    unittest.main()