def test_duplicate(arraynums):
    num_counts = {}
    for num in arraynums:
        if num in num_counts:
            return True
        else:
            num_counts[num] = 1
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_duplicate([1,2,3,4,5]), False)

if __name__ == '__main__':
    unittest.main()