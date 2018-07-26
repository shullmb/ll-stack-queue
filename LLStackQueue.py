# from LinkedList import Node
from LinkedList import LinkedList

class Stack:
  def __init__(self):
    self.store = LinkedList()

  def push(self, data):
    self.store.add(data)
    return self.store
  
  def pop(self):
    
    pass
  
  def print_stack(self):
    self.store.print_list()

stack = Stack()

stack.push("one")
stack.push("two")

# stack.print_stack()

class Queue:
  def __init__(self):
    self.store = LinkedList()
  
  def enqueue(self, data):
    self.store.add(data)
    return self.store
  
  def dequeue(self):
    data = self.store.delete_at_head()
    return data

  def print_queue(self):
    self.store.print_list()


queue = Queue()
queue.enqueue('one')
queue.enqueue('two')
queue.enqueue('three')
queue.enqueue('four')
queue.enqueue('five')

test = queue.dequeue()
print(test)