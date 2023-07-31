## Linked List
## Hash Table

### Date: 07/29/2023

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = collections.OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # mark key as recently used
        self.cache.move_to_end(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # modify value
            self.cache[key]=value
            # mark key as recently used
            self.cache.move_to_end(key)
            return 

        if len(self.cache) >= self.cap:
            self.cache.popitem(last=False)
        self.cache[key] = value




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)