# class Node:
#     def ___init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} #key -> node
        self.cap  = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        #linked the nodes
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node
        
        

    def get(self, key: int) -> int:
        #if key is present: get key, reorder, return val
        #else, return -1
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        #if key is already present, reorder 
        #manually put/update new key/val
        
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        #if capacity is full, remove lru, delete it's key
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



##def __init__(self, capacity: int):
#         #store cache as list of lists[key,value], with most recently used(MRU) at the end and 
#         #Least recently used(LRU) at the begining
#         self.cache = []
#         self.capacity = capacity
       
#     def get(self, key: int) -> int:
#         for i in range(len(self.cache)):
#             if self.cache[i][0] == key:
#                 tmp = self.cache.pop(i)
#                 self.cache.append(tmp)
#                 return tmp[1]
#         return -1

#     def put(self, key: int, value: int) -> None:
#         for i in range(len(self.cache)):
#             if self.cache[i][0]== key:
#                 tmp = self.cache.pop(i)
#                 tmp[1] = value
#                 self.cache.append(tmp)
#                 return
#         #if capacity is reached, meaning we can no longer add a new item, pop the least recently used item
#         if self.capacity==len(self.cache) :
#             self.cache.pop(0)
#         self.cache.append([key,value])
        