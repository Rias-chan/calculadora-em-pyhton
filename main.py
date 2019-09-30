import raiz
import math
import texto

def soma():
  print('Digite the 2 numbers')
  numero1 = input()
  numero2 = input()
  return float(numero1) + float(numero2)

def sub():
  print('Digite the 2 numbers')
  sub1 = input()
  sub2 = input()
  return float(sub1) - float(sub2)

def multi():
  print('Digite the 2 numbers')
  multi1 = input()
  multi2 = input()
  return float(multi1)*float(multi2)

def div():
  print('Digite the 2 numbers')
  div1 = input()
  div2 = input()
  if(div2 == '0'):
    return 'Não da tiozãum, 0 é numero de tarado'
  return float(div1)/float(div2)

#Funções da segunda parte
def soma2(menor):
  print('Digite um numero para ser somado: ')
  soma0 = input()
  return float(soma0)

def sub2(menor):
  print('Digite um numero para ser subtraido: ')
  sub0 = input()
  return float(sub0)

def multi2(menor):
  print('Digite um numero para ser multiplicado: ')
  multi0 = input()
  return float(multi0)
  
def div2(menor):
  print('Digite um numero para ser dividido: ')
  div0 = input()
  return float(div0)

#========================== main ================================
menor = 0
terminar = 't'
texto.match()
escolha = input()

if (escolha == '1'):
  menor = soma()
  texto.resultado(menor)
  texto.cor()
  terminar = input()
elif (escolha == '2'):
  menor = sub()
  texto.resultado(menor)
  texto.cor()
  terminar = input()
elif (escolha == '3'):
  menor = multi()
  texto.resultado(menor)
  texto.cor()
  terminar = input() 
elif (escolha == '4'):
  menor = div()
  texto.resultado(menor)
  texto.cor()
  terminar = input()
elif (escolha == '5'):
  menor = raiz.raiz(menor)
  texto.resultado(menor)
else: 
  print ('Bora pro putero jao')
  
#Vai para a segunda parte/segundas funções caso o usuario queira efetuar mais alguma operação

while (terminar != 'q' and terminar == 't'):
  texto.match()
  escolha = input()
  if (escolha == '1'):
    menor = menor + soma2(menor)
    texto.resultado(menor)
    texto.cor()
    terminar = input()
  elif (escolha == '2'):
    menor = menor - sub2(menor)
    texto.resultado(menor)
    texto.cor()
    terminar = input()
  elif (escolha == '3'):
    menor = float(menor) * multi2(menor)
    texto.resultado(menor)
    texto.cor()
    terminar = input()
  elif (escolha == '4'):
    menor = float (menor)/div2(menor)
    texto.resultado(menor)
    texto.cor()
    terminar = input()
  elif (escolha == '5'):
    texto.resultado(math.sqrt(menor))
    menor = math.sqrt(menor)
    texto.cor()
    terminar = input()
  elif (escolha):
    terminar = 'q'
    print('Mama only by 99')

#https://www.gov.uk again⌛