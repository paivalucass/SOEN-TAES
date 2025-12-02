def get_total_number_of_sequences(m, n):
    total_sequences = 0
    for element in range(1, m//2+1):
        total_sequences += (m//(2*element))**(n-1)
    return total_sequences
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_total_number_of_sequences(10, 4), 4)

if __name__ == '__main__':
    unittest.main()