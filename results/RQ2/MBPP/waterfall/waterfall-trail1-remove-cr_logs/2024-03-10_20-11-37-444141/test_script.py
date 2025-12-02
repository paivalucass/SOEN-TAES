def get_lucid_numbers(n):
    if n <= 0:
        return []
    lucid_numbers = [1]
    for current_num in range(2, n + 1):
        is_lucid = True
        for i in range(2, int(current_num ** 0.5) + 1):
            if current_num % i == 0:
                is_lucid = False
                break
        if is_lucid:
            lucid_numbers.append(current_num)
    return lucid_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()