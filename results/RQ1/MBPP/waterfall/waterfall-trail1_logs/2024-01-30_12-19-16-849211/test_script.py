def test_duplicate(arraynums):
    '''Write a function to find whether a given array of integers contains any duplicate element.'''
    if not arraynums or not all(isinstance(x, int) for x in arraynums):
        return False
    seen = set()
    for num in arraynums:
        if num in seen:
            return True
        seen.add(num)
    return False

assert test_duplicate([1,2,3,4,5])==False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_duplicate([1,2,3,4,5]), False)

if __name__ == '__main__':
    unittest.main()