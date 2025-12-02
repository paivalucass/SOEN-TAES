def pluck(arr):
    smallest_even_value = float('inf')
    smallest_even_index = -1
    
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < smallest_even_value:
            smallest_even_value = arr[i]
            smallest_even_index = i
            
    if smallest_even_index == -1:
        return []
    
    return [smallest_even_value, smallest_even_index]
import unittest

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(pluck([4,2,3]), [2, 1])

    def test_example2(self):
        self.assertEqual(pluck([1,2,3]), [2, 1])

    def test_example3(self):
        self.assertEqual(pluck([]), [])

    def test_example4(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

if __name__ == '__main__':
    unittest.main()