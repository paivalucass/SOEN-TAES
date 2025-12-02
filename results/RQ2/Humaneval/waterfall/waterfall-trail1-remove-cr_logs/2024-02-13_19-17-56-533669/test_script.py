def incr_list(l: list) -> list:
    if not isinstance(l, list) or len(l) == 0:
        return []

    if len(l) > 10000:
        raise ValueError("Exceeded maximum list size of 10,000 elements")

    for num in l:
        if not isinstance(num, int):
            raise ValueError("Elements must be integers")
        if num < 1 or num > 1000:
            raise ValueError("Elements must be within the valid range of 1 to 1000")

    return [x + 1 for x in l]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4])
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124])

if __name__ == '__main__':
    unittest.main()