def Split(list):
    if len(list) == 0:
        return []
    
    odd_list = [num for num in list if num % 2 != 0]
    
    return odd_list

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Split([1,2,3,4,5,6]), [1,3,5])

if __name__ == '__main__':
    unittest.main()