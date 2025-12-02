def diff(li1: list[int], li2: list[int]) -> list[int]:
    if not li1 and not li2:
        return []
    if any(not isinstance(item, int) for item in li1 + li2):
        raise ValueError("Input lists should only contain integers")
    result = [item for item in li1 if item not in li2]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]), [10, 20, 30, 15])

if __name__ == '__main__':
    unittest.main()