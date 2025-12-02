def reverse_Array_Upto_K(input, k): 
    if not isinstance(input, list) or not all(isinstance(x, (int, float)) for x in input):
        return "Invalid input: input should be a list of integers or floats"
    
    if k < 0 or k >= len(input):
        return "Invalid input: k is out of range"
    
    return input[:k][::-1] + input[k:]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6], 4), [4, 3, 2, 1, 5, 6])

if __name__ == '__main__':
    unittest.main()