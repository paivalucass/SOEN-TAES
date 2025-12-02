def find_Max_Num(arr) :
    if not arr or not all(isinstance(x, int) for x in arr):
        return "Invalid input"
    
    if all(num < 0 for num in arr):
        return "Negative integers not allowed"
    
    arr.sort(reverse=True)
    
    largest_num = int(''.join(map(str, arr)))
    
    return largest_num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Max_Num([1,2,3]), 321)

if __name__ == '__main__':
    unittest.main()