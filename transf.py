class Transf(object):

  def __init__(self):
    self.prior = -1

  def getPrior(self):
    return self.prior

  def conversao(self, valor):
    if valor == '^':
      self.prior = 3
    elif valor == '*' or valor == '/' or valor == 'x' or valor == ':':
      self.prior = 2
    elif valor == '+' or valor == '-':
      self.prior = 1
    elif valor == ')' or valor == '(':
      self.prior = 0
    elif valor == 'a':
      self.prior = -1

  def compare(self, prior, newPrior):
    return newPrior > prior