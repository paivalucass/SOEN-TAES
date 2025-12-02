def sum_even_and_even_index(arr):
    even_numbers_at_even_positions = [arr[i] for i in range(len(arr)) if i % 2 == 0 and arr[i] % 2 == 0]
    return sum(even_numbers_at_even_positions)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_even_and_even_index([5, 6, 12, 1, 18, 8]), 30)

if __name__ == '__main__':
    unittest.main()