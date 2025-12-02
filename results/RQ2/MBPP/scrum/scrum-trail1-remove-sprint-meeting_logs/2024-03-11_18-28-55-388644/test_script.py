def get_total_number_of_sequences(m, n):
    if n == 1:
        return m
    else:
        return (m // 2) * get_total_number_of_sequences(m // 2, n - 1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_total_number_of_sequences(10, 4), 4)

if __name__ == '__main__':
    unittest.main()