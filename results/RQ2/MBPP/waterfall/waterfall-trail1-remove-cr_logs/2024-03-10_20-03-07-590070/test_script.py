def rearrange_bigger(n):
    try:
        if type(n) != int or n <= 0:
            raise ValueError("Input must be a positive integer")
        
        num_str = list(str(n))
        for i in range(len(num_str) - 1, 0, -1):
            if num_str[i] > num_str[i - 1]:
                num_str[i], num_str[i - 1] = num_str[i - 1], num_str[i]
                return int(''.join(num_str))
        
        raise ValueError("Input is already the largest possible number with the given digits")
    except ValueError as e:
        return str(e)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rearrange_bigger(12), 21)

if __name__ == '__main__':
    unittest.main()