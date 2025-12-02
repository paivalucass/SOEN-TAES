def sum_even_and_even_index(arr):
    sum_even_at_even_pos = 0
    for index, number in enumerate(arr):
        if index % 2 == 0 and number % 2 == 0:
            sum_even_at_even_pos += number
    return sum_even_at_even_pos
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_even_and_even_index([5, 6, 12, 1, 18, 8]), 30)

if __name__ == '__main__':
    unittest.main()