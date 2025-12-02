def get_max_sum(n):
    '''
    Write a function to find the maximum sum possible by using the given equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n).
    assert get_max_sum(60) == 106
    '''
    if not isinstance(n, int):
        return "InputError"
    elif n < 0:
        return "InputError"
    elif n == 0:
        return 0
    elif n <= 5:
        return n
    else:
        return max(get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5), n)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_max_sum(60), 106)

if __name__ == '__main__':
    unittest.main()