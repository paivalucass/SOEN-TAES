def colon_tuplex(tuplex, m, n):
    try:
        if not isinstance(tuplex, tuple):
            raise TypeError("Input data type is not a tuple")
        
        if not isinstance(m, int) or m < 0 or m > len(tuplex):
            raise TypeError("Invalid index value")
        
        result = list(tuplex)
        result.insert(m, n)
        
        return tuple(result)
    
    except (TypeError, IndexError) as e:
        print("Error:", e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(colon_tuplex(("HELLO", 5, [], True), 2, 50), ("HELLO", 5, [50], True))

if __name__ == '__main__':
    unittest.main()