class Node():
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

class Queue():
  def __init__(self, value = None):
    self.front = None
    self.rear = None
    self.size = 0

    if value is not None:
      self.enqueue(value)

  def isEmpty(self):
    return self.size == 0

  # add item in end of the queue
  def enqueue(self, value):
    nodeTemporary = Node(value)
    if self.front is None:
      self.front = nodeTemporary
      self.rear = nodeTemporary
    else:
      # changes address of old rear
      self.rear.next = nodeTemporary
      # changes the last element
      self.rear = nodeTemporary

    self.size += 1

  def dequeue(self):
    if self.isEmpty():
      print('ERROR: Queue empty')
    else:
      data = self.front.value
      self.front = self.front.next
      self.size -= 1
    return data

  def getTop(self):
    if self.isEmpty():
      print('ERROR: Queue empty')
      return None
    else:
      value = self.front.value
      return value

  def getSize(self):
    return self.size

  def clear(self):
    while not self.isEmpty():
      value = self.dequeue()

  def __str__(self):
    helperQueue = Queue()

    strQueue = ''
    while not self.isEmpty():
      value = self.dequeue()
      helperQueue.enqueue(value)
      strQueue += str(value) + ' '
      
    while not helperQueue.isEmpty():
      value = helperQueue.dequeue()
      self.enqueue(value)
      
    return strQueue

queue = Queue()
queue.enqueue(3)
queue.enqueue(5)
print(queue)

      