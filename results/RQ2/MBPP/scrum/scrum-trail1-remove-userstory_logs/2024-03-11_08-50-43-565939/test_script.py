def test_duplicate(arraynums):
    frequency_map = {}
    for num in arraynums:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    
    for key, value in frequency_map.items():
        if value > 1:
            return True
    
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_duplicate([1,2,3,4,5]), False)

if __name__ == '__main__':
    unittest.main()