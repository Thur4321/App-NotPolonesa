class Pilha(object):

  def __init__(self, len):
    self.topo = -1
    self.vet = ['a'] * len

  def push(self, valor):
    self.topo += 1
    self.vet[self.topo] = valor

  def pop(self):
    aux = self.topo
    self.topo -= 1
    return self.vet[aux]

  def isEmpty(self):
    return self.topo == -1

  def prin(self):
    print(self.vet)

  def vetor(self):
    arr = []
    for i in self.vet:
      if i != 'a':
        arr.append(i)
    return arr