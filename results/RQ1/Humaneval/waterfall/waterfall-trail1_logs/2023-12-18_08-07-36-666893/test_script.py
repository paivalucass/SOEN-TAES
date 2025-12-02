from typing import List

def below_zero(operations: List[int]) -> bool:
    if not operations:
        raise ValueError("Input list cannot be empty")
    for op in operations:
        if not isinstance(op, int):
            raise ValueError("Input list must only contain integer values")
    
    def calculate_balance(operations: List[int]) -> int:
        balance = 0
        for op in operations:
            balance += op
            if balance < 0:
                return True
        return False

    return calculate_balance(operations)

import unittest

class Test(unittest.TestCase):
    def test_below_zero_false(self):
        self.assertEqual(below_zero([1, 2, 3]), False)

    def test_below_zero_true(self):
        self.assertEqual(below_zero([1, 2, -4, 5]), True)

if __name__ == '__main__':
    unittest.main()