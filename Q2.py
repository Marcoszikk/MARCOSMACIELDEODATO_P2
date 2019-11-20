#A)

def invertmatrix(a,b,c,d):
  detA = a.d - b.c
  if detA == 0:
    return none
  else:
    
    
    
    
#B)

def main(a,b,c,d):

  a = int(input('Insira o valor do indice (0,0):'))
  b = int(input('Insira o valor do indice (0,1):'))
  c = int(input('Insira o valor do indice (1,0):'))
  d = int(input('Insira o valor do indice (1,1):'))

linha1 = [a , b]
linha2 = [c , d]

matrix = [linha1, linha2]
print ('Essa é sua matriz')
print(matrix)

print('Essa é sua matriz inversa:')
print(invertmatrix(a, b, c, d))
