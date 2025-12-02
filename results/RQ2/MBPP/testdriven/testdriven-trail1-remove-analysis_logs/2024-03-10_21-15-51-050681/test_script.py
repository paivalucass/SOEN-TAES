def max_sub_array_sum_repeated(a, n, k):
    max_sum = float('-inf')
    current_sum = 0
    
    for _ in range(k):
        temp_sum = 0
        for num in a:
            temp_sum += num
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        current_sum = max(current_sum, temp_sum)
    
    return max_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3), 30)

if __name__ == '__main__':
    unittest.main()