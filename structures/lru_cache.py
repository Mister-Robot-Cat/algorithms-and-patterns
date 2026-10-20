"""LRU (Least Recently Used) Cache implementation using Doubly Linked List & Hash Map."""
from typing import Dict, Optional, Any
from dataclasses import dataclass

@dataclass
class Node:
    key: Any
    value: Any
    prev: Optional["Node"] = None
    next: Optional["Node"] = None

class LRUCache:
    """Least Recently Used (LRU) Cache.
    
    Provides O(1) get and put operations.
    """
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive integer")
        self.capacity = capacity
        self.cache: Dict[Any, Node] = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node

    def _add_to_front(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next
        if self.head.next:
            self.head.next.prev = node
        self.head.next = node

    def get(self, key: Any) -> Optional[Any]:
        if key not in self.cache:
            return None
        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value

    def put(self, key: Any, value: Any) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add_to_front(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            if lru_node and lru_node != self.head:
                self._remove(lru_node)
                del self.cache[lru_node.key]

# Refined on 2026-10-20
