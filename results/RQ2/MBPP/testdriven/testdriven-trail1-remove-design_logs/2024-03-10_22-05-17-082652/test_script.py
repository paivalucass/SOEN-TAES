def colon_tuplex(tuplex, m, n):
    '''
    Write a function to get a colon of a tuple.
    assert colon_tuplex(("HELLO", 5, [], True), 2, 50) == ("HELLO", 5, [50], True)
    '''
    if not isinstance(tuplex, tuple):
        raise TypeError
    
    if m < 0:
        raise ValueError
    
    if m >= len(tuplex):
        raise IndexError
    
    return tuplex[:m] + ([n],) + tuplex[m+1:]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(colon_tuplex(("HELLO", 5, [], True), 2, 50), ("HELLO", 5, [50], True))

if __name__ == '__main__':
    unittest.main()