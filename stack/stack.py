class Stack:
  def __init__ (self, stackSize):
    self.top = -1
    self.size = stackSize
    self.stack = [None] * stackSize
  
  # Incrementa o tamanho da pilha e insere o novo valor
  def push(self, value):
    self.top += 1
    self.stack[self.top] = value

  # Remove o item do topo da lista e retorna seu valor
  def pop(self):
    if(self.top == -1):
      return
    helper = self.stack[self.top]
    self.top -= 1
    return helper

  # Cheio se o índice no topo + 1 for igual a capacidade informada no inicio
  def isFull(self):
    return self.top + 1 == self.size

  # Vazio se possui seu valor inicial -1
  def isEmpty(self):
    return self.top == -1

  # Pega o elemento no topo da lista
  def top(self):
    return self.stack[self.top]

  # Pega o tamanho da lista + 1 por ter iniciado com -1 na instancia
  def stackSize(self):
    return str(self.top + 1)
  
  # Clona a pilha, removendo os itens e depois devolve esses valores.
  def __str__(self):
    cloneStack = Stack(self.size)

    while not self.isEmpty():
      value = self.pop()
      cloneStack.push(value)

    helper = '['
    while not cloneStack.isEmpty():
      cloneValue = cloneStack.pop()
      self.push(cloneValue)
      helper +=  ' ' + str(cloneValue)
    helper += ' ]'

    return helper

stack = Stack(2)
print(stack.isEmpty())
stack.push(5)
stack.push(2)
print(stack.isEmpty())
print(stack.stackSize())
print(stack.isFull())
print(stack)
stack.pop()
print(stack)