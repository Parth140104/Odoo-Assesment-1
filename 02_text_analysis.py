import re
from collections import Counter, defaultdict
import heapq

STOP_WORDS = {
    'the', 'is', 'at', 'on', 'in', 'and', 'a', 'an', 'to', 'of', 'for', 'with', 'that', 'this', 'it', 'as', 'by'
}

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.words = set()

class WordFrequencyAnalyzer:
    def __init__(self, text):
        self.counter = Counter()
        self.trie_root = TrieNode()
        self._process_text(text)

    def _process_text(self, text):
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        filtered_words = [word for word in words if word not in STOP_WORDS]
        self.counter = Counter(filtered_words)
        for word in self.counter:
            self._insert_into_trie(word)

    def _insert_into_trie(self, word):
        node = self.trie_root
        for char in word:
            node = node.children[char]
            node.words.add(word)

    def query_top_k_with_prefix(self, prefix, k):
        node = self.trie_root
        for char in prefix.lower():
            if char not in node.children:
                return []
            node = node.children[char]
        word_freqs = [(self.counter[word], word) for word in node.words]
        top_k = heapq.nlargest(k, word_freqs)
        return [word for freq, word in top_k]

text = """
This is the text of the paragraph. The program should find the most common words in this paragraph and allow 
quick search functionality based on prefixes. The threshold for the top words can be configured.
"""

analyzer = WordFrequencyAnalyzer(text)

print("Top 3 words starting with 'th':", analyzer.query_top_k_with_prefix('th', 3))
