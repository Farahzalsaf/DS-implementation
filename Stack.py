class Stack:
    
    # constructor
    def __init__(self):
        self._data = []
    
    # check if stack is empty
    def is_empty(self):
        return len(self._data)==0
    
    # main operations
    def push(self,e):
        self._data.append(e)
    
    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            return self._data.pop()
        
    # Auxiliary operations
    def __len__(self):
        return len(self._data)
    
    def top(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            return self._data[-1]
        
    
        
        
        