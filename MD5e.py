import math



"""con el organiza el valor dado , primero asegurandose que la longitud del 
valor sea exactamente de 32, luego con un nuevo string concatena los valores dados del 
primer valor entregado  """
def reorganizar(bitString32):
 if len(bitString32) != 32:
  raise ValueError("Necesita una longitud de 32")
 newString = ""
 for i in [3,2,1,0]:
  newString += bitString32[8*i:8*i+8]
 return newString





"""Reformatea el valor ,dandole en inicio 08x , luego de forma progresiva concatenamos"""

def reformatear_HEXA(i):
 hexrep = format(i,'08x')
 thing = ""
 for i in [3,2,1,0]:
  thing += hexrep[2*i:2*i+2]
 return thing




"""Concatena el valor dado para que llegue a los 512 bits , luego le da la finalidad en
 format 064b para finalmente reorganizarlo , y retornar el valor modificado"""
 
def pad(bitString):
 startLength = len(bitString)
 bitString += '1'
 while len(bitString) % 512 != 448:
  bitString += '0'
 lastPart = format(startLength,'064b')
 bitString += reorganizar(lastPart[32:]) + reorganizar(lastPart[:32]) 
 return bitString





def Obtener_Bloque(bitString):
 corrientePos = 0
 while corrientePos < len(bitString):
  currPart = bitString[corrientePos:corrientePos+512]
  mySplits = []
  for i in range(16):
   mySplits.append(int(reorganizar(currPart[32*i:32*i+32]),2))
  yield mySplits
  corrientePos += 512




""" retorna un valor entero dado en el inicio , con una relacion de solo 2 de longitud"""
def not32(i):
 i_str = format(i,'032b')
 new_str = ''
 for c in i_str:
  new_str += '1' if c=='0' else '0'
 return int(new_str,2)





""" retorna el residuo de la suma de 2 valores dados , entre el valor 2 elevado
 a la 32"""
def resid32_sum(a,b):
 return (a + b) % 2**32






def leftrot32(i,s):
 return (i << s) ^ (i >> (32-s))









def md5me(testString):
 bs =''
 for i in testString:
  bs += format(ord(i),'08b')
 bs = pad(bs)

 tvals = [int(2**32 * abs(math.sin(i+1))) for i in range(64)]

 a0 = 0x67452301
 b0 = 0xefcdab89
 c0 = 0x98badcfe
 d0 = 0x10325476

 s = [7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22, 
  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20, 
  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23, 
  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21 ]












 for m in Obtener_Bloque(bs):
  A = a0 
  B = b0
  C = c0
  D = d0
  for i in range(64):
   if i <= 15:
    #f = (B & C) | (not32(B) & D)
    f = D ^ (B & (C ^ D))
    g = i
   elif i<= 31:
    #f = (D & B) | (not32(D) & C)
    f = C ^ (D & (B ^ C))
    g = (5*i+1) % 16
   elif i <= 47:
    f = B ^ C ^ D
    g = (3*i+5) % 16
   else:
    f = C ^ (B | not32(D))
    g = (7*i) % 16
   dtemp = D
   D = C
   C = B
   B = resid32_sum(B,leftrot32((A + f + tvals[i] + m[g]) % 2**32, s[i]))
   A = dtemp
  a0 = resid32_sum(a0, A)
  b0 = resid32_sum(b0, B)
  c0 = resid32_sum(c0, C)
  d0 = resid32_sum(d0, D)

 digest = reformatear_HEXA(a0) + reformatear_HEXA(b0) + reformatear_HEXA(c0) + reformatear_HEXA(d0)
 return digest

def Ejecutar():
    mensaje = "Profe_quiero_20"
    hash_md5 = md5me(mensaje)
    print('"%s" = %s' % (mensaje, hash_md5))

if __name__ == "__main__":
 Ejecutar()
