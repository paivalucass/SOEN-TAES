from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    
    if not all(isinstance(operation, int) for operation in operations):
        raise TypeError("The input must be a list of integers")
    
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    
    return False
import unittest

class Test(unittest.TestCase):
    def test_below_zero_false(self):
        self.assertEqual(below_zero([1, 2, 3]), False)

    def test_below_zero_true(self):
        self.assertEqual(below_zero([1, 2, -4, 5]), True)

if __name__ == '__main__':
    unittest.main()