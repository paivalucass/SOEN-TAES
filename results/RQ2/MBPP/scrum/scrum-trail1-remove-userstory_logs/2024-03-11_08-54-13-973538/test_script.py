def count(boolean_list):
    try:
        count = 0
        if len(boolean_list) == 0:
            raise ValueError("Input list is empty")
        
        for item in boolean_list:
            if not isinstance(item, bool):
                raise TypeError("Non-boolean value found in the list")
            
            if item:
                count += 1
        
        return count
    except (ValueError, TypeError) as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count([True,False,True]), 2)

if __name__ == '__main__':
    unittest.main()