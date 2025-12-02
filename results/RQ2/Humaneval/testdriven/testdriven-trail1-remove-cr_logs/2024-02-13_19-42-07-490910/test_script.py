def string_sequence(n: int) -> str:
    if n < 0:
        raise ValueError("Input 'n' should be a non-negative integer.")

    sequence = []

    for i in range(n+1):
        sequence.append(str(i))

    return ' '.join(sequence)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(string_sequence(0), '0')
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

if __name__ == '__main__':
    unittest.main()