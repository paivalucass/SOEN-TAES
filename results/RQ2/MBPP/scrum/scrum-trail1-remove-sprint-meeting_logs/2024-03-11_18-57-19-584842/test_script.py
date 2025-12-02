def get_ludic(n):
    ludic_numbers = [1]
    x = 2
    while len(ludic_numbers) < n:
        is_ludic = True
        for i in range(2, x):
            if x % i == 0:
                is_ludic = False
                break
        if is_ludic:
            ludic_numbers.append(x)
        x += 1
    return [num for num in ludic_numbers if num <= n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()