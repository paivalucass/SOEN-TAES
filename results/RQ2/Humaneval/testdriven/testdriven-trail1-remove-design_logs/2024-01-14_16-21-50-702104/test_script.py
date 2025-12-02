def count_numbers_starting_or_ending_with_one(n: int) -> int:
    count = 0
    if isinstance(n, int) and n > 0:
        for i in range(10 ** (n - 1), 10 ** n):
            if str(i)[0] == '1' or str(i)[:-1] == '1':
                count += 1
        return count
    else:
        return 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(starts_one_ends(1), 1)
        self.assertEqual(starts_one_ends(2), 11)
        self.assertEqual(starts_one_ends(3), 20)

if __name__ == '__main__':
    unittest.main()