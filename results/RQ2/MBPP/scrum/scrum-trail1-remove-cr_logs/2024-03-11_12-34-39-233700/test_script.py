def find_equal_tuple(Input):
    if len(Input) < 2:
        return True
    else:
        length = len(Input[0])
        for item in Input:
            if len(item) != length:
                return False
        return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_equal_tuple([(11, 22, 33), (44, 55, 66)]), True)

if __name__ == '__main__':
    unittest.main()