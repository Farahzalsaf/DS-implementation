class Stack:
    
    
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self,element,nxt=None):
            self._element = element
            self._next = nxt
            
        def get_next(self): return self._next
        def set_next(self,n): self._next = n
        def get_data(self): return self._element
        def set_data(self,d): self._element = d

    
    def __init__(self):
        self.top = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    
    def __len__(self): return self.size
    
    
    def push(self,d):
        self.top = self._Node(d,self.top)
        self.size += 1
    
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else:
            temp = self.top._element
            self.top = self.top._next
            self.size -= 1
            return temp
    
    
    def first(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        else: 
            return self.top._element
    
    
    