def largest_subset(a):
    if len(a) < 2:
        return 0
    
    graph = {i: [] for i in range(len(a))}
    
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j and a[j] % a[i] == 0:
                graph[i].append(j)

    def dfs(node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    largest = 0
    for start_node in range(len(a)):
        visited = set()
        dfs(start_node, visited)
        largest = max(largest, len(visited))

    return largest
import unittest

class Test(unittest.TestCase):
    def test_largest_subset(self):
        self.assertEqual(largest_subset([1, 3, 6, 13, 17, 18]), 4)

if __name__ == '__main__':
    unittest.main()