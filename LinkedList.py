
class Node:
    __slots__ = '_element', '_nxt'
    
    def __init__(self,element,nxt=None):
        self._element = element
        self._nxt = nxt
        
    def get_next(self): return self._nxt
    def set_next(self,n): self._nxt = n
    def get_data(self): return self._element
    def set_data(self,d): self._element = d
    
class LinkedList:
    
    def __init__(self,r = None):
        self.root = r
        self.size = 0
    
    def get_size(self):
        return self.size
    
    
    def add(self,d):
        new_node = Node(d,self.root)
        self.root = new_node
        self.size += 1
    
    def remove(self,d):
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
    
    def find(self,d):
        this_node = self.root
        while this_node:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None
    

'''
lst = LinkedList()
lst.add(4)
lst.add(10)
lst.remove(10)
lst.find(4)
lst.find(10)
'''
                
        
        