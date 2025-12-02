def find_First_Missing(array, start=0, end=None):
    if end is None:
        end = len(array)
    
    if not isinstance(array, list) or not all(isinstance(x, int) for x in array) or not isinstance(start, int) or not isinstance(end, int):
        return "Input validation error: 'array' parameter must be a list and 'start' and 'end' parameters must be integers."

    if end < 0 or end > len(array):
        return "Error: 'end' parameter is out of range or negative."

    for i in range(end):
        if array[i] != i:
            return i
    
    return end
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_First_Missing([0,1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()