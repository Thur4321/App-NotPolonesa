class Fila(object):

  def __init__(self, len):
    self.topo = -1
    self.fim = -1
    self.vet = ['a'] * len

  def push(self, valor):
    self.topo += 1
    self.vet[self.topo] = valor

  def pop(self):
    self.fim += 1
    return self.vet[self.fim]

  def isFull(self):
    return self.topo == len(self.vet)-1

  def isEmpty(self):
    return self.fim == len(self.vet)-1
 
  def prin(self):
    eq = ''
    for i in range(0, len(self.vet)):
      if self.vet[i] == 'a' or self.vet[i] == '(' or self.vet[i] == ')':
        pass
      else:
        eq = eq + ' ' + self.vet[i]
    return eq