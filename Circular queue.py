class CircularQueue:
  def __init__(self, maxSize):
    self.queue = list()
    self.maxSize = maxSize
    self.front = 0
    self.rear = 0
  
  def enqueue(self, data):
    if self.size() == (self.maxSize - 1):
      return("Queue is full!")
    else:
      self.queue.append(data)
      self.rear = (self.rear+1) % self.maxSize
      return True
  
  def dequeue(self):
    if self.size() == 0:
      return("Queue is empty!")
    else:
      data = self.queue[self.front]
      self.front = (self.front+1) % self.maxSize
      return data
  
  def size(self):
    if self.rear >= self.front:
      qSize = self.rear - self.front
    else:
      qSize = self.maxSize - (self.front - self.rear)
    return qSize
size = input("Enter the size of the Circular Queue:")
q = CircularQueue(int(size))
print(q.enqueue(10))
print(q.enqueue(20))
print(q.enqueue(30))
print(q.enqueue(70))
print(q.enqueue(80))
print(q.dequeue())
print(q.dequeue())
#print(q.dequeue())
#print(q.dequeue())
print(q.size())