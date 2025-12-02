def amicable_numbers_sum(limit):
    amicable_nums = {}
    total_sum = 0
    
    for num in range(1, limit):
        divisor_sum = sum([i for i in range(1, num) if num % i == 0])
        amicable_nums[num] = divisor_sum
    
    for key, value in amicable_nums.items():
        if value in amicable_nums and amicable_nums[value] == key and value != key:
            total_sum += key
    
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(amicable_numbers_sum(999), 504)

if __name__ == '__main__':
    unittest.main()