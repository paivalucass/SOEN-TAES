def get_total_number_of_sequences(m, n):
    if n == 1:
        return m
    elif n == 2:
        return (m-1) // 2
    else:
        return sum(get_total_number_of_sequences(i, n-1) for i in range(1, m//2 + 1))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_total_number_of_sequences(10, 4), 4)

if __name__ == '__main__':
    unittest.main()