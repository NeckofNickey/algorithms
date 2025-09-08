class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def heapify_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < self.size and self.heap[left] < self.heap[min_index]:
            min_index = left
        
        if right < self.size and self.heap[right] < self.heap[min_index]:
            min_index = right
        
        if i != min_index:
            self.swap(i, min_index)
            self.heapify_down(min_index)
    
    def push(self, value):
        self.heap.append(value)
        self.size += 1
        self.heapify_up(self.size - 1)
    
    def pop(self):
        if self.size == 0:
            return None
        
        root = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.heap.pop()
        self.size -= 1
        self.heapify_down(0)
        return root
    
    def peek(self):
        return self.heap[0] if self.size > 0 else None
    
    def is_empty(self):
        return self.size == 0
   
    
heap = MinHeap()