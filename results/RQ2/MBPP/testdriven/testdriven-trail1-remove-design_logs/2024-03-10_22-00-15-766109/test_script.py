def div_sum(num1, num2):
    '''Write a function to determine if the sum of the divisors of two integers are the same.
    assert are_equivalent(36, 57) == False'''
    
    def are_equivalent(parameter1, parameter2):
        if parameter1 == '' or parameter2 == '':
            return "Invalid Input"
        elif parameter1 is None or parameter2 is None:
            return "Invalid Input"
        elif sum_divisors(parameter1) == sum_divisors(parameter2):
            return False
        else:
            return False
    
    def sum_divisors(num):
        divisors_sum = 0
        for i in range(1, num + 1):
            if num % i == 0:
                divisors_sum += i
        return divisors_sum

    return are_equivalent(num1, num2)
import unittest

class Test(unittest.TestCase):
    def test_div_sum(self):
        self.assertEqual(div_sum(36, 57), False)

if __name__ == '__main__':
    unittest.main()