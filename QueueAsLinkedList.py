class Queue:
    
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self,element,nxt=None):
            self._element = element
            self._next = nxt
            
            
        
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    
    def __len__(self): return self._size
    
    def is_empty(self): return self._size == 0
    
    
    def first(self):
        if self.is_empty(): raise Exception("Queue is empty")
        else:
            return self._head._element
    
    
    # main operations
    def enqueue(self,d):
        new_node = self._Node(d)
        
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1
        
    
    
    def dequeue(self):
        if self.is_empty(): raise Exception("Queue is empty")
        else:
            answer = self._head._element
            self._head = self._head._next
            self._size -=1
            if self.is_empty():
                self._tail = None
                
            return answer
    
            
    
    def __str__(self):
        start = self._head
        s = '['
        while start:
            s += str(start._element)
            s += ','
            start = start._next
            
        return s + ']'
    
    
    