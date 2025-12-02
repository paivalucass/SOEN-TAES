from typing import Union

def maximum(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    '''
    Write a python function to find the maximum of two numbers.
    assert maximum(5,10) == 10
    '''
    return max(a, b)
import unittest

class Test(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(maximum(5, 10), 10)

if __name__ == '__main__':
    unittest.main()