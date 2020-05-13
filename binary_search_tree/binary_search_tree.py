import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack



class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
                return
            else:
                self.left.insert(value)

        if value >= self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
                return
            else:
                self.right.insert(value)
    

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == None:
            return False
    
        elif self.value == target:
            return True
        else:
            print(f'target: {target}, self.value: {self.value}')
            if target >= self.value:
                if self.right == None:
                    return False
                else:
                    return self.right.contains(target)
            elif target <= self.value:
                if self.left == None:
                    return False
                else:
                    return self.left.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else: 
            return self.right.get_max()
        
    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value == None:
            return
        cb(self.value)
        print(f'self.left: {self.left}')
        print(f'self.right: {self.right}')
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)


        # def in_order(node, c):
        #     print(f'node value: {node.value}')
        #     if node.value == None:
        #         return
        #     c(node.value)
        #     in_order(node.left, c)
        #     in_order(node.right, c)

        # in_order(self, cb)
        
        
        
    

       

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

b = BinarySearchTree(5) #node
b.insert(2)
b.insert(3)
b.insert(7)
print(b.for_each(print))
