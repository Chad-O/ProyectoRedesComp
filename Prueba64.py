import base64 as b64p

class Base64(object):
    charLista = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

#Algoritmo de particionado en base a input de cantidad de 'partes'
    def particion(self, data, length):
        return [data[i:i+length] for i in range(0, len(data), length)]

#Inicio Codificacion
    def codificar(self, data):
        padding = 0
        if len(data) % 3 != 0:
            padding = (len(data) + 3 - len(data) % 3) - len(data)
        #Separación para saber cuántos "padding" se necesitan
        data += b"\x00"*padding

        p3 = self.particion(data, 3)

#Transformación a string binario
        binstring = ""
        for particion in p3:
            for x in particion:
                binstring += "{:0>8}".format(bin(x)[2:])

#División de bloques/particiones de 6 bits por string.
        p6 = self.particion(binstring, 6)

        outstring = ""
        for element in p6:
            outstring += self.charLista[int(element, 2)]
            #Agregar el '=' por la cantidad de padding necesario
        outstring = outstring[:-padding] + "="*padding
        return outstring
#Fin Codificacion

"""     def decodificar(self, data):
        padding = data.count("=")
        data = data.replace("=", "A")
        print(padding)
        binstring = ""
        for char in data:
            binstring += "{:0>6b}".format(self.charLista.index(char))

        octavos = self.parte(binstring, 8)
        
        outbytes = b""
        for parte in octavos:
            outbytes += bytes([int(parte, 2)])

        return outbytes[:-padding] """

if __name__ == "__main__":
    b64 = Base64()
    stringValidacion = b"Hello"
    print("Algoritmo implementado:")
    print(b64.codificar(stringValidacion))
    print("Libería base64:")
    print(b64p.b64encode(stringValidacion))