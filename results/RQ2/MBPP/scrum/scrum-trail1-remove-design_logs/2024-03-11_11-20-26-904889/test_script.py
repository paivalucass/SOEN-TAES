def max_sum_list(lists):
    if not lists:
        return None
    
    max_list = max(lists, key=sum)
    return max_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]), [10, 11, 12])

if __name__ == '__main__':
    unittest.main()