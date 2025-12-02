def max_sub_array_sum(a, size):
    if not a or size > len(a):
        return 0
    
    max_sum = current_sum = a[0]
    
    for num in a[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8), 7)

if __name__ == '__main__':
    unittest.main()