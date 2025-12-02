def start_withp(words):
    result = [word for word in words if word.lower().startswith('p')]
    if len(result) < 2:
        return tuple(result)
    raise ValueError("No words starting with 'p'")
import unittest

class Test(unittest.TestCase):
    def test_start_withp(self):
        self.assertEqual(start_withp(["Python PHP", "Java JavaScript", "c c++"]), ('Python', 'PHP'))

if __name__ == '__main__':
    unittest.main()