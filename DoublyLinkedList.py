class DoublyLinkedList:
    
    # inner class
    class _Node:
        __slots__ = '_element', '_prev', '_next'
        
        def __init__(self,element,prev,nxt):
            self._element = element
            self._prev = prev
            self._next = nxt
            
    # end of inner class
    
    
    def __init__(self):
        self._head = None
        self._size = 0
        
    
    def insert_at_head(self,d):
        new_node = self._Node(d,None,self._head)
        if self._head: self._head._prev = new_node
        
        self._head = new_node
        self._size += 1
        
        return new_node
        
    
    def insert_between(self,d,pred,succ):
        new_node = self._Node(d,pred,succ)
        pred._next = new_node
        succ._prev = new_node
        self._size += 1
        return new_node
    
    def delete_node(self,node):
        pred = node._prev
        succ = node._next
        pred._next = succ
        succ._prev = pred
        self._size -= 1
        
        answer = node._element
        node._prev = node._element = node._next = None
        return answer
    
    
    def _print(self):
        start = self._head
        while start:
            print(start._element,end=' ')
            start = start._next
    
    
    