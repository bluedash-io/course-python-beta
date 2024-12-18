import unittest
from problem_1 import shortestDistance

class TestShortestDistance(unittest.TestCase):
    def test_cases(self):
        # Test Case 1
        wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
        word1 = "coding"
        word2 = "practice"
        self.assertEqual(shortestDistance(wordsDict, word1, word2), 3)

        # Test Case 2
        wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
        word1 = "makes"
        word2 = "coding"
        self.assertEqual(shortestDistance(wordsDict, word1, word2), 1)

if __name__ == "__main__":
    unittest.main()
