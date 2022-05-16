class Conta(object):

  def __init__(self):
    pass
    
  def operacao(self, v1, v2, op):
    if op == '+':
        res = v1 + v2
    elif op == '-':
        res = v1 - v2
    elif op == '/' or op == ':':
        res = v1 / v2
    elif op == '*' or op == 'x':
        res = v1 * v2
    elif op == '^':
        res = v1 ** v2
    return res