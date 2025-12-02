def count_integer(list1):
    try:
        if not isinstance(list1, list):
            raise TypeError("Input should be a list")
        
        count = 0
        for item in list1:
            if isinstance(item, int):
                count += 1
        return count
    
    except TypeError as e:
        print(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_integer([1,2,'abc',1.2]), 2)

if __name__ == '__main__':
    unittest.main()