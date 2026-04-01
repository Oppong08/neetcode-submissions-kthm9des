#bruteforce list
class LRUCache:

    def __init__(self, capacity: int):
        #store cache as list of lists[key,value], with most recently used(MRU) at the end and 
        #Least recently used(LRU) at the begining
        self.cache = []
        self.capacity = capacity
       
    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                self.cache.append(tmp)
                return tmp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0]== key:
                tmp = self.cache.pop(i)
                tmp[1] = value
                self.cache.append(tmp)
                return
        #if capacity is reached, meaning we can no longer add a new item, pop the least recently used item
        if self.capacity==len(self.cache) :
            self.cache.pop(0)
        self.cache.append([key,value])
        
       















#map: keep track of capacity, 
#have a hashmap with key pointing (instead of storing) to nodes
#have a doubly linked list for easy swap/removal of least recently used
#each node having a previous pointer and a next pointer
#have tw0 dummy nodes left and right node to temporarily hold the least and most rececntly used cache
#if we're puting/inserting a new node, we put it in between the left and right nodes
#need remove/insert helper functions to update most recently used cache into our linked list(left and right holder)
# class Node:
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cap = capacity 
#         self.cache = {} #maps key to node
#         self.left, self.right = Node(0,0), Node(0,0) #hasmap to store least/most recently used cache
#         self.left.next = self.right
#         self.right.prev = self.left


#     def remove(self, node):# remove from our linked list
#         prev, nxt = node.prev, node.next
#         prev.next = nxt
#         nxt.prev = prev

#     def insert(self, node): # insert into ther rightmost position in our linked list
#         prev, nxt = self.right.prev, self.right
#         prev.next = nxt.prev = node
#         node.next, node.prev = nxt, prev

#     def get(self, key: int) -> int:
#         #return value at key
#         if key in self.cache:
#             #Todo : update most recently used
#             self.remove(self.cache[key]) #remove from the list
#             self.insert(self.cache[key]) # add to the right most position
#             return self.cache[key].val 
#         else:
#             return - 1

#     def put(self, key: int, value: int) -> None:
#         #update capacity, add new - value
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key])
        
#         if len(self.cache) > self.cap:
#             #if insertion makes our cahce store more than the capacity:
#             #remove from the list and delete LRU from the haashmap
#             lru = self.left.next
#             self.remove(lru)
#             del self.cache[lru.key]

