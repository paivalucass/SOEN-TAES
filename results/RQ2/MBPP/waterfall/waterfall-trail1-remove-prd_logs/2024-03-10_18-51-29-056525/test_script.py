def start_withp(words):
    if not isinstance(words, list) or not all(isinstance(w, str) for w in words):
        raise ValueError("Input 'words' must be a list of strings")
    
    p_words = [word for word in words for word in word.split() if word.lower().startswith('p')]
    
    return tuple(p_words[:2]) if len(p_words) >= 2 else "Handle appropriately"
import unittest

class Test(unittest.TestCase):
    def test_start_withp(self):
        self.assertEqual(start_withp(["Python PHP", "Java JavaScript", "c c++"]), ('Python', 'PHP'))

if __name__ == '__main__':
    unittest.main()