class Node:
  def __init__(self, data = None, left = None, right = None):
    self.data = data
    self.left = left
    self.right = right

class Tree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    if self.root is None:
      self.root = Node(value)
      return
    self._add(value, self.root)

  def _add(self, value, node):
    if value > node.data:
      if node.right is None:
        node.right = Node(value)
      else:
        self._add(value, node.right)
      return

    if node.left is None:
      node.left = Node(value)
    else:
      self._add(value, node.left)

  def printTree(self):
    if self.root is None:
      print('The tree is empty')
      return
    self._printTree(self.root)

  def _printTree(self, node):
    if node is not None:
      self._printTree(node.left)
      print(str(node.data) + ' ')
      self._printTree(node.right)
  
  def search(self, value):
    if self.root is None:
      print('The tree is empty')
      return

    actual = self.root
    while actual.data != value:
      if value > actual.data:
        actual = actual.right
      else:
        actual = actual.left
      if actual is None:
        return False
    return True

tree = Tree()
tree.printTree()

tree.insert(2)
tree.insert(5)
tree.insert(1)
tree.insert(4)
tree.insert(3)
tree.printTree()
print('Item encontrado: ', tree.search(6))