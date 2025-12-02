def start_withp(words):
    if not all(isinstance(word, str) for word in words):
        raise ValueError("Input list should contain only string elements")
    
    p_words = [word for word in words for word in word.split() if word.lower().startswith('p')]
    
    return tuple(p_words)
import unittest

class Test(unittest.TestCase):
    def test_start_withp(self):
        self.assertEqual(start_withp(["Python PHP", "Java JavaScript", "c c++"]), ('Python', 'PHP'))

if __name__ == '__main__':
    unittest.main()