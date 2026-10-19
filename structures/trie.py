"""Prefix Tree (Trie) implementation for fast autocomplete and prefix matching."""
from typing import Dict, List, Optional

class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.is_end_of_word: bool = False

class Trie:
    """Prefix Tree supporting insert, search, and prefix matching."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return bool(node and node.is_end_of_word)

    def starts_with(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def autocomplete(self, prefix: str) -> List[str]:
        results: List[str] = []
        node = self._find_node(prefix)
        if not node:
            return results

        def dfs(current_node: TrieNode, path: str):
            if current_node.is_end_of_word:
                results.append(path)
            for char, next_node in current_node.children.items():
                dfs(next_node, path + char)

        dfs(node, prefix)
        return results
