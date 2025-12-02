def is_equal_to_sum_even(n):
    count = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            count += 1
    return count == 4

test_values = [0, 1, -1, 4, 6, 8, 10]
for value in test_values:
    result = is_equal_to_sum_even(value)
    print(f"is_equal_to_sum_even({value}) = {result}")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_equal_to_sum_even(4), False)
        self.assertEqual(is_equal_to_sum_even(6), False)
        self.assertEqual(is_equal_to_sum_even(8), True)

if __name__ == '__main__':
    unittest.main()