import time

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    cache_limit = 5                 # setting limit
    flag = False                    # If True, prints cache list

    def __init__(self, func):
        self.func = func
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __call__(self, *args, **kwargs):
        # If in cache, pull results
        if args in self.cache:
            self.llist(args)
            if self.flag == True:
                return f'{args}\n{self.cache[args]}\n {self.cache}'
            return self.cache[args]

        # If cache-limit reached - Remove LRU from node link list and dict - cache.
        if self.cache_limit is not None:
            if len(self.cache) > self.cache_limit:
                n = self.head.next
                self._remove(n)
                del self.cache[n.key]

        # Compute and cache and node - if not in cache
        result = self.func(*args, **kwargs)
        self.cache[args] = result
        node = Node(args, result)
        self._add(node)
        if self.flag == True:
            return f'{result}\nCache: {self.cache}'
        return result

    # Remove from double linked-list - Node.
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    # Add to double linked-list - Node.
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    # If in result in cache, move to top of Cache/linked-list - Node.
    def llist(self, args):
        current = self.head
        while True:
            if current.key == args:
                node = current
                self._remove(node)
                self._add(node)
                if self.flag == True:
                    del self.cache[node.key]
                    self.cache[node.key] = node.val
                break
            else:
                current = current.next

@LRUCache
def ex_func_01(n):
    time.sleep(1)
    return n*n

print("First Implementation")
print(ex_func_01(1))
print(ex_func_01(2))
print(ex_func_01(3))
print(ex_func_01(4))
print(ex_func_01(5))
print(ex_func_01(6))

#Faster--> Since already in cache
print(f'\n Function: Second Implementation')
print(ex_func_01(6))
print(ex_func_01(5))
print(ex_func_01(4))
print(ex_func_01(3))
print(ex_func_01(2))
print(ex_func_01(1))
