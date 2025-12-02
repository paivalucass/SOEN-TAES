def find_equal_tuple(Input):
    if not isinstance(Input, list):
        return False
    if not all(isinstance(item, tuple) for item in Input):
        return False
    if len(Input) < 1:
        return False
    
    length = len(Input[0])
    for tup in Input:
        if len(tup) != length:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_equal_tuple([(11, 22, 33), (44, 55, 66)]), True)

if __name__ == '__main__':
    unittest.main()