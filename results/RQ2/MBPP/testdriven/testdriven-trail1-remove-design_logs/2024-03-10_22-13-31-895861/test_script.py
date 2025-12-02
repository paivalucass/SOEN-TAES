def get_ludic(n):
    '''Write a function to get all lucid numbers smaller than or equal to a given integer.
    assert get_ludic(10) == [1, 2, 3, 5, 7]'''
    if n < 1:
        return []
    elif n == 1:
        return [1]
    else:
        ludic_numbers = [1, 2]
        num = 3
        while len(ludic_numbers) < n:
            is_ludic = True
            for i in ludic_numbers:
                if num % i == 0:
                    is_ludic = False
                    break
            if is_ludic:
                ludic_numbers.append(num)
            num += 1
        return ludic_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()