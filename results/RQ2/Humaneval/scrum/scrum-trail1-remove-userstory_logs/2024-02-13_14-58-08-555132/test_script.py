from typing import List

def below_zero(operations: List[int]) -> bool:
    if operations is None or len(operations) == 0:
        return "Error: Input list of operations is empty or None"

    balance = 0

    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    
    return False
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(below_zero([1, 2, 3]), False)

    def test2(self):
        self.assertEqual(below_zero([1, 2, -4, 5]), True)

if __name__ == '__main__':
    unittest.main()