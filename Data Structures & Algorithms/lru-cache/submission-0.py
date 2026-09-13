class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}  # key -> Node

        # Dummy head and tail
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # Remove node from linked list
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        # Add node right after head
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]

        # Move node to head
        self._remove(node)
        self._add_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]

            # Update value
            node.value = value

            # Move to head
            self._remove(node)
            self._add_to_head(node)

        else:
            # Create new node
            node = Node(key, value)

            # Add to hashmap
            self.map[key] = node

            # Add to head
            self._add_to_head(node)

            # Remove least recently used node
            if len(self.map) > self.capacity:
                lru = self.tail.prev

                self._remove(lru)
                del self.map[lru.key]

