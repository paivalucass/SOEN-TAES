def sum_range_list(list1, m, n):
    try:
        if len(list1) == 0:
            return "Error handling for empty input list"
        
        if m < 0 or n < 0 or m >= len(list1) or n >= len(list1) or m > n:
            return "Error handling for invalid indices"
        
        return sum(list1[m:n+1])
    except Exception as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10), 29)

if __name__ == '__main__':
    unittest.main()