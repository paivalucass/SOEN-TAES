def eat(number, need, remaining):
    assert isinstance(number, int), "number must be an integer"
    assert isinstance(need, int), "need must be an integer"
    assert isinstance(remaining, int), "remaining must be an integer"
    
    assert 0 <= number <= 1000, "number must be within 0 and 1000"
    assert 0 <= need <= 1000, "need must be within 0 and 1000"
    assert 0 <= remaining <= 1000, "remaining must be within 0 and 1000"
    
    if remaining < need:
        return [number + remaining, 0]
    else:
        return [number + need, remaining - need]
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(eat(5, 6, 10), [11, 4])

    def test2(self):
        self.assertEqual(eat(4, 8, 9), [12, 1])

    def test3(self):
        self.assertEqual(eat(1, 10, 10), [11, 0])

    def test4(self):
        self.assertEqual(eat(2, 11, 5), [7, 0])

if __name__ == '__main__':
    unittest.main()