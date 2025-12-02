def max_sub_array_sum(a, size):
    max_sum = a[0]
    current_sum = a[0]
    
    for i in range(1, size):
        current_sum = max(a[i], a[i] + current_sum)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8), 7)

if __name__ == '__main__':
    unittest.main()