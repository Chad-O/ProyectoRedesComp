import hashlib

"""
msg='Profe_quiero_20'
resultado = hashlib.md5(msg.encode()) 

print(msg+" -> ENCONDE MD5 -> "+ resultado.hexdigest())

"""



md5 = hashlib.md5()
md5.update('Profesor: Hola,cuanta nota deseas obtener.'.encode())
md5.update('Alumno: Hola, me gustaria 20 pero con un 18 me conformo.'.encode())
md5.update('Profesor: Se que te esforzaste , te mereces un 15 '.encode())
md5.update('Alumno:Almenos no desaprobe el curso :,v '.encode())
print("ENCODE MD5 CONVERSACION:"+md5.hexdigest())

