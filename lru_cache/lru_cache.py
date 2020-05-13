from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.storage = DoublyLinkedList()
        #self.current = len(self.storage)
        self.storage_dict = {}
        self.size = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage_dict:
            node = self.storage_dict[key]
            self.storage.move_to_end(node)
            print(node)
            print(node.value)
            print(node.value[1])
            print(node.value[0])
            return node.value[1]
        else:
            return None
        # self.storage.add_to_tail(self.storage_dict[key])
        # return self.storage_dict[key]

        
    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage_dict:
            node = self.storage_dict[key]
            node.value = (key, value)
            self.storage.move_to_end(node)
            return
        if self.size == self.limit:
            del self.storage_dict[self.storage.head.value[0]]
            self.storage.remove_from_head()
            self.size += 1

        self.storage.add_to_tail((key, value))
        self.storage_dict[key] = self.storage.tail
        self.size += 1

        # self.storage_dict.update({key, value})
        # ##not sure if this following will work because self.storage.key is funky linked
        # if self.current == self.limit:
        #     self.storage_dict.pop(self.storage.tail.key)
        #     self.storage.remove_from_tail()
        # if self.storage.key and self.storage.key is not self.storage.head:
        #     self.storage.delete(self.storage.key)
        #     self.storage.add_to_head({key, value})
        # if self.storage.key == self.storage.head:
        #     self.storage.key = value



        


        



