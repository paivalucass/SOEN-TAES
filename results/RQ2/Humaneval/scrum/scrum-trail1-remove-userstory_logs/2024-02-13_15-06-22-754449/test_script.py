def pairs_sum_to_zero(input_list):
    seen_numbers = set()

    for num in input_list:
        if -num in seen_numbers:
            return True
        seen_numbers.add(num)

    return False
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(pairs_sum_to_zero([1, 3, 5, 0]), False)

    def test2(self):
        self.assertEqual(pairs_sum_to_zero([1, 3, -2, 1]), False)

    def test3(self):
        self.assertEqual(pairs_sum_to_zero([1, 2, 3, 7]), False)

    def test4(self):
        self.assertEqual(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]), True)

    def test5(self):
        self.assertEqual(pairs_sum_to_zero([1]), False)

if __name__ == '__main__':
    unittest.main()