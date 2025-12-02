def max_sub_array_sum_repeated(a, n, k):
    if not a or k <= 0:
        return 0
    
    modified_array = a * k
    
    max_sum = float('-inf')
    current_sum = 0
    
    for num in modified_array:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3), 30)

if __name__ == '__main__':
    unittest.main()