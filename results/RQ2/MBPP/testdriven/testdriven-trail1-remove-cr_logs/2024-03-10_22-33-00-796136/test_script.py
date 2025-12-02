def div_sum(integer1, integer2):
    '''
    Determines if the sum of the divisors of two integers are the same.
    
    Parameters:
    integer1 (int): First integer
    integer2 (int): Second integer
    
    Returns:
    bool: True if the sum of divisors of both integers are the same, False otherwise
    '''
    def sum_of_divisors(n):
        return sum([i for i in range(1, n) if n % i == 0])
    return sum_of_divisors(integer1) == sum_of_divisors(integer2)

# Test Cases
assert div_sum(6, 28) == True  # Expected output: True
assert div_sum(36, 57) == False  # Expected output: False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(are_equivalent(36, 57), False)

if __name__ == '__main__':
    unittest.main()