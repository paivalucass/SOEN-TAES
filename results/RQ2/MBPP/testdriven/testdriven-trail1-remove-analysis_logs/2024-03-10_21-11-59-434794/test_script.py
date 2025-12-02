def find_solution(coeff_a, coeff_b, target_sum):
    """
    Write a function that returns integers x and y that satisfy ax + by = n as a tuple, 
    or return None if no solution exists.
    """
    for x in range(target_sum + 1):
        y = (target_sum - coeff_a * x) / coeff_b
        if y.is_integer():
            return (x, int(y))
    return None
assert find_solution(2, 3, 7) == (2, 1)
import unittest

class Test(unittest.TestCase):
    def test_find_solution(self):
        self.assertEqual(find_solution(2, 3, 7), (2, 1))

if __name__ == '__main__':
    unittest.main()