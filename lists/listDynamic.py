class Node:
    def __init__(self, data = None, next = None, previous = None):
      self.data = data
      self.next = next
      self.previous = previous

class List:
    def __init__(self):
      self.head = None
      self.tail = None
      self.size = 0

    # Insert in the head
    def pushHead(self, data):
      tempNode = Node(data)

      if self.head is None:
        self.head = tempNode
        self.tail = self.head

      else:
        # o previous do head anterior agora aponta para o novo nó
        self.head.previous = tempNode
        # next do novo nó será o head antes de ser mudado
        tempNode.next = self.head
        # o novo head recebe o novo nó
        self.head = tempNode
      self.size += 1

    # Insert in the end of the list
    def pushTail(self, data):
      tempNode = Node(data)

      if self.head is None:
        self.head = tempNode
        self.tail = self.head

      else:
        # próximo item antes de atualizar é o novo nó
        self.tail.next = tempNode
        # vincula o anterior com o último elemento
        tempNode.previous = self.tail
        # atribui após o valor do nó após o processo de vinculações entre nós
        self.tail = tempNode
      self.size += 1

    # Insert in a position
    def insert(self, data, position):
      tempNode = Node(data)
      helperHead = self.head
      for iterator in range(1, position):
        helperHead = helperHead.next
      tempNode.next = helperHead.next
      tempNode.previous = helperHead
      helperHead.next.previous  = tempNode
      helperHead.next  = tempNode
      self.size += 1

    # Return size of the list
    def getSize(self):
      return self.size

    # Return if the list is empty
    def isEmpty(self):
      return self.head is None

    # Remove the first value
    def removeHead(self):
      temp = self.head
      self.head = self.head.next
      self.size -= 1
      return temp

    # Remove the last value
    def removeTail(self):
      temp = self.tail
      # o próximo depois do anterior do último (antigo último) passa a ser None
      self.tail.previous.next = None
      # o último agora é o anterior
      self.tail = self.tail.previous
      self.size -= 1
      return temp

    # Remove a value in x position
    def remove(self, position):
      helperHead = self.head
      iterator = 1
      while (iterator <= position):
        helperHead = helperHead.next
        iterator += 1

      if position == 0:
        self.head = self.head.next
      else:
        helperHead.previous.next = helperHead.next
      
      if position == self.size - 1:
        self.tail = self.tail.previous
      else:
        helperHead.next.previous = helperHead.previous
      self.size -= 1

    # Search value in list
    def search(self, value):
      tempNode = self.head
      tempValue = tempNode.data
      if (tempValue == value):
        return 0

      index = 1
      while tempNode.next is not None:
        tempNode = tempNode.next
        tempValue = tempNode.data

        if tempValue == value:
          return index
        index += 1
      return -1

    # Print all values in list
    def __str__(self):
      items = ''
      nodeTemporary = self.head
      while nodeTemporary != None:
        items += str(nodeTemporary.data) + ' '
        nodeTemporary = nodeTemporary.next
      return items

list = List()

list.pushHead(2)
list.pushHead(1)
list.pushTail(3)
list.pushTail(5)
list.insert(4, 3)
print('List (insert): ' + str(list))
print('Search: ' + str(list.search(5)))

list.removeTail()
list.removeHead()
print('List (removeTail, removeHead): ' + str(list))

list.remove(2)
print('List (remove()): ' + str(list))

list.removeTail()
print('List (removeTail): ' + str(list))
