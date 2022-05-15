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
    # if the value is bigger than node, insert in the right
    if value > node.data:
      if node.right is None:
        node.right = Node(value)
      # go throught right node if the right node is not None
      else:
        self._add(value, node.right)
      return
    
    # if the value is lower than node, insert in the left
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
    # print left and right until be None
    if node is not None:
      self._printTree(node.left)
      print(str(node.data) + ' ')
      self._printTree(node.right)
  
  def search(self, value):
    if self.root is None:
      print('Tree Error: The tree is empty')
      return

    actual = self.root
    while actual.data != value:
      # if value is bigger than node data, seach in right
      if value > actual.data:
        actual = actual.right
      # if value is lower than node data, seach in left
      else:
        actual = actual.left
      if actual is None:
        return False
    return True


######################################################################

tree = Tree()
tree.printTree()

tree.insert(2)
tree.insert(5)
tree.insert(1)
tree.insert(4)
tree.insert(3)
tree.printTree()
print('Item encontrado: ', tree.search(6))