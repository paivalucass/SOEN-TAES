def test_duplicate(arraynums):
    num_set = set()
    for num in arraynums:
        if num in num_set:
            return True
        num_set.add(num)
    return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(test_duplicate([1,2,3,4,5]), False)

if __name__ == '__main__':
    unittest.main()