class LRUCache(object):
    class Node(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev, self.next = None, None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.dict = {}
        self.head, self.tail = self.Node(-1, -1), self.Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _insert(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next.prev = node
        self.head.next = node
        
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self._remove(node)
        self._insert(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            node.value = value
            self._insert(node)
        else:
            if self.size == self.capacity:
                evict = self.tail.prev
                self._remove(evict)
                del self.dict[evict.key]
                self.size -= 1
            node = self.Node(key, value)
            self.dict[key] = node
            self._insert(node)
            self.size += 1
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
