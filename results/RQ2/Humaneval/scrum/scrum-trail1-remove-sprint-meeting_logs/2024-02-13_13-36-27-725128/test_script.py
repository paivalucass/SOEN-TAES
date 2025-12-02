from typing import List

def below_zero(operations: List[int]) -> bool:
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False
import unittest
from typing import List

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(below_zero([1, 2, 3]), False)
    
    def test2(self):
        self.assertEqual(below_zero([1, 2, -4, 5]), True)

if __name__ == '__main__':
    unittest.main()