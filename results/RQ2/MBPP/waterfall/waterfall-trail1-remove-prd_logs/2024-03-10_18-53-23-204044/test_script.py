def is_polite(n):
    if n < 1:
        return 0
    polite_nums = [1]
    i = 2
    while len(polite_nums) < n:
        count = 0
        for j in range(1, i):
            if len(polite_nums) >= j:
                count += polite_nums[-j]
            else:
                break
            if count >= i:
                polite_nums.append(i)
                break
        i += 1
    return polite_nums[n-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_polite(7), 11)

if __name__ == '__main__':
    unittest.main()