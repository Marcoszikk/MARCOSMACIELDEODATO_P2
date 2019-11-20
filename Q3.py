def isCollisionDetected(BLx, BLy, TRx, TRy):
  
  if BLx > TRx or BLx < TRx and BLy > TRy or BLy < TRy:
    
    return false
  
  else:
    return true
    
  
def main(BLx, BLy, TRx, TRy):

  BLx = float(input('Insira o valor do bottom lef x:'))
  BLy = float(input('Insira o valor do bottom lef y:'))
  TRx = float(input('Insira o valor do top right x:'))
  TRy = float(input('Insira o valor do top right y:'))
  
  if isCollisionDetected(BLx, BLy, TRx, TRy) == false:
    
    print('Colisão não detectada')
  
  else:
    
    print('Colisão detectada')
    
