from pilha import Pilha

from fila import Fila

from transf import Transf

from conta import Conta

import sys

class Main(object):

  contas = ['+', '-', '*', 'x', '/', ':', '^']

  nota = input('Qual a expressão? \n')

  p3 = Pilha(len(nota))

  t = Transf()

  c = Conta()

  for i in nota:
      if p3.isEmpty():
          p3.push(i)
      else:
          if i.isnumeric():
              valor = p3.pop()
              if valor.isnumeric():
                  newValor = '' + valor + i
                  p3.push(newValor)
              else:
                  p3.push(valor)
                  p3.push(i)
          else:
              p3.push(i)

  newNota = p3.vetor()

  f = Fila(len(newNota))

  p = Pilha(len(newNota))

  f2 = Fila(len(newNota))

  p2 = Pilha(len(newNota))

  p4 = Pilha(len(newNota))

  paren = 0
  num = 0
  operadores = 0

  for i in newNota:
    if i == '(' or i == ')':
      paren += 1
    elif i.isnumeric():
      num += 1
    elif i in contas:
      operadores += 1

  if operadores != num-1:
    sys.exit('Equação falta operadores')
  elif paren%2 != 0:
    sys.exit('Equação falta parênteses')
  
  
  for i in newNota:
    f2.push(i)
   
  while f2.isEmpty() == False:     
    val = f2.pop()        
    if val.isnumeric():
      f.push(val)
    else:
      prior = t.getPrior()
      t.conversao(val)
      newPrior = t.getPrior()
      if p2.isEmpty():
        p2.push(val)
      else:
        if t.compare(prior, newPrior):
            p2.push(val)
        else:
            if val == '(':
              p2.push(val)
            else:
              if val == ')':
                operador = p2.pop()
                while operador != '(' and p2.isEmpty() != True:
                  f.push(operador)
                  operador = p2.pop()
                if p2.isEmpty() == False:
                  newoperador = p2.pop()
                  t.conversao(newoperador)
                  p2.push(newoperador)
              else:
                while t.compare(prior, newPrior) == False:
                  operador = p2.pop()
                  if operador == '(':
                    p2.push(operador)
                    break
                  else:
                    f.push(operador)
                    if p2.isEmpty():
                      t.conversao('a')
                      break
                t.conversao(val)    
              p2.push(val)

  while p2.isEmpty() == False:
      operar = p2.pop()
      f.push(operar)

  print('Expressão original: ', nota, '\nExpressão pós-fixada: ', f.prin())

  pos = 0
  while f.isEmpty() == False:
    op = f.pop()
    if op.isnumeric():
      p.push(float(op))
      p4.push(op)
    elif op in contas:
      v2 = p.pop()
      v1 = p.pop()
      val2 = p4.pop()
      val1 = p4.pop()
      resultado = c.operacao(v1, v2, op)
      p.push(resultado)
      variavel = 't' + str(pos)
      if val1.isnumeric() and val2.isnumeric():
        print(variavel, '=', int(v1), ' ', op, ' ', int(v2), ' = ', int(resultado))
      else:
        if val2.isnumeric():
          print(variavel, '=', val1, ' ', op, ' ', int(val2), '->', val1, ' = ', int(v1), '->', int(v1), ' ', op, '', int(v2), ' = ', int(resultado))
        elif val1.isnumeric():
            print(variavel, '=', int(val1), ' ', op, ' ', val2, '->', val2, ' = ', int(v2), '->', int(v1), ' ', op, '', int(v2), ' = ', int(resultado))
        else:
            print(variavel, '=', val1, ' ', op, ' ', val2, '->', val1, ' = ', int(v1), '->', val2, ' = ', int(v2), '->', int(v1), ' ', op, '', int(v2), ' = ', int(resultado))

      pos += 1
      p4.push(variavel)

  print('Resultado final: ', resultado)

  input('Tecle enter para finalizar')