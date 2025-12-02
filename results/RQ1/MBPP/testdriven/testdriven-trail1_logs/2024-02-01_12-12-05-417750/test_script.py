def div_sum(n):
    def find_divisors(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return divisors
    
    def calculate_sum(divisors):
        return sum(divisors)
    
    def are_equivalent(num1, num2):
        if sum(find_divisors(num1)) == sum(find_divisors(num2)):
            return False
        else:
            return True

    assert are_equivalent(36, 57) == False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(are_equivalent(36, 57), False)

if __name__ == '__main__':
    unittest.main()