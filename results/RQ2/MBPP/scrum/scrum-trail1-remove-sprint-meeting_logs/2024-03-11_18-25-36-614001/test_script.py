def div_sum(n):
    def get_divisors(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return divisors
    
    def sum_divisors(divisors):
        return sum(divisors)
    
    def are_equivalent(num1, num2):
        divisors1 = get_divisors(num1)
        divisors2 = get_divisors(num2)
        
        sum1 = sum_divisors(divisors1)
        sum2 = sum_divisors(divisors2)
        
        return sum1 == sum2
    
    return are_equivalent(36, 57)
import unittest

class Test(unittest.TestCase):
    def test_div_sum(self):
        self.assertEqual(div_sum(36), False)

if __name__ == '__main__':
    unittest.main()