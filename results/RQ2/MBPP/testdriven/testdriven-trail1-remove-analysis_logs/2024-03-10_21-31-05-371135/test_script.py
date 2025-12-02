def is_perfect_square(n):
    # Binary search algorithm to check for perfect square
    start_number = 1
    end_number = n
    while start_number <= end_number:
        mid_number = (start_number + end_number) // 2
        if mid_number * mid_number == n:
            return True
        elif mid_number * mid_number < n:
            start_number = mid_number + 1
        else:
            end_number = mid_number - 1
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_perfect_square(10), False)

if __name__ == '__main__':
    unittest.main()