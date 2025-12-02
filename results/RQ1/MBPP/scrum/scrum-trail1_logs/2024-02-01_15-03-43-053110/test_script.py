from typing import Union, Tuple

def swap_numbers(a: Union[int, float], b: Union[int, float]) -> Tuple[Union[int, float], Union[int, float]]:
    return (b, a)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_numbers(10, 20), (20, 10))

if __name__ == '__main__':
    unittest.main()