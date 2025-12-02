def Split(list): 
    if len(list) == 0:
        return "Error: Input list is empty"
    
    if not all(isinstance(x, int) for x in list):
        return "Error: Input should be a list of integers"
    
    result = [] 
    
    for num in list:
        if num % 2 != 0:
            result.append(num)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Split([1,2,3,4,5,6]), [1,3,5])

if __name__ == '__main__':
    unittest.main()