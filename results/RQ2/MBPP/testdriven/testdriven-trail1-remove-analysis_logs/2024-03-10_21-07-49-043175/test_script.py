def test_duplicate(input_array):
    seen_elements = set()
    
    for num in input_array:
        if num in seen_elements:
            return True
        seen_elements.add(num)
    
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_duplicate([1,2,3,4,5]), False)

if __name__ == '__main__':
    unittest.main()