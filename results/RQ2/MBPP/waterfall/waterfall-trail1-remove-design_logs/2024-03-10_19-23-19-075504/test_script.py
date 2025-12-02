def reverse_Array_Upto_K(input, k):
    reversed_elements = input[:k]
    reversed_elements.reverse()
    return reversed_elements + input[k:]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4), [4, 3, 2, 1, 5, 6])

if __name__ == '__main__':
    unittest.main()