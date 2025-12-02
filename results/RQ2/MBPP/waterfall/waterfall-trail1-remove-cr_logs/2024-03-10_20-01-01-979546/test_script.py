def start_withp(words):
    try:
        words = [word for word in words if word.lower().startswith('p')]
        words = [word.split() for word in words]
        words = [item for sublist in words for item in sublist]
        if len(words) >= 2:
            return tuple(words[:2])
        elif len(words) == 1:
            return words[0], ''
        else:
            raise ValueError("No words starting with 'p' found")
    except Exception as e:
        raise ValueError("Invalid input or empty list")
Here is a python test script in unittest framework for the given question:

```python
import unittest

class Test(unittest.TestCase):
    def test_start_withp(self):
        self.assertEqual(start_withp(["Python PHP", "Java JavaScript", "c c++"]), ('Python', 'PHP'))

if __name__ == '__main__':
    unittest.main()
```

This script defines a function `start_withp` to return two words from a list of words starting with letter 'p', and then uses `unittest` framework to test the function with the given input and output.