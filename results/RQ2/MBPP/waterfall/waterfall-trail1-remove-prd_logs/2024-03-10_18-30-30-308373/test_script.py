def div_sum(n1, n2):
    def sum_of_divisors(num):
        div_sum = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                div_sum += i
                if i != num // i:
                    div_sum += num // i
        return div_sum
    
    return sum_of_divisors(n1) == sum_of_divisors(n2)
import unittest

class Test(unittest.TestCase):
    def test_div_sum(self):
        self.assertEqual(div_sum(36, 57), False)

if __name__ == '__main__':
    unittest.main()