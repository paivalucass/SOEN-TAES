def multiple_to_single(L):
    if not L:
        raise ValueError("Input list cannot be empty")

    if not all(isinstance(num, int) for num in L):
        raise ValueError("Input list must contain only integers")

    str_list = [str(num) for num in L]
    result = int("".join(str_list))

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiple_to_single([11, 33, 50]), 113350)

if __name__ == '__main__':
    unittest.main()