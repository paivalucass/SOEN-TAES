def sequence(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"
    newman_conway_sequence = [0, 1]
    if n <= 2:
        return newman_conway_sequence[n - 1]
    for i in range(3, n+1):
        next_element = newman_conway_sequence[newman_conway_sequence[i-1] - 1] + newman_conway_sequence[i - newman_conway_sequence[newman_conway_sequence[i-1] - 1] - 1]
        newman_conway_sequence.append(next_element)
    return newman_conway_sequence[n - 1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequence(10), 6)

if __name__ == '__main__':
    unittest.main()