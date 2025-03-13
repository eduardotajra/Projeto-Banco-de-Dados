class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def setNext(self, next):
        self.next = next