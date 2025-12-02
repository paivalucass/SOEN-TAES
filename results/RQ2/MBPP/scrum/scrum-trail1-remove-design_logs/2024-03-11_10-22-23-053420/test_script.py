def even_Power_Sum(n):
    if n <= 0:
        return "Error: Input should be a positive integer"
    
    sum_of_evens_to_fifth_power = sum(i ** 5 for i in range(2, n*2+1, 2))
    return sum_of_evens_to_fifth_power
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_Power_Sum(2), 1056)

if __name__ == '__main__':
    unittest.main()