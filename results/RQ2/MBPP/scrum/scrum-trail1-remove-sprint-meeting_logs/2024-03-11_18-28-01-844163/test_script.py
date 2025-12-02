def larg_nnum(list1, n):
    if not all(isinstance(x, (int, float)) for x in list1):
        raise ValueError("list1 should contain only numeric values")
    
    if n <= 0:
        raise ValueError("n should be greater than 0")

    if not list1:
        return []

    sorted_list = sorted(list1, reverse=True)

    return sorted_list[:n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2), [100, 90])

if __name__ == '__main__':
    unittest.main()