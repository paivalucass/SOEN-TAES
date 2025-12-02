def is_decimal(num):
    if not isinstance(num, str): 
        return False
    
    if not num.replace('.', '', 1).isdigit():
        return False
    
    parts = num.split('.')
    if len(parts) != 2 or len(parts[1]) != 2:
        return False
    
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_decimal('123.11'), True)

if __name__ == '__main__':
    unittest.main()