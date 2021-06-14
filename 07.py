""" num=10
num='20'
if type(num)==int:
    num = num*2
else:
   print('El valor no es numerico')

def mensaje(msg):
    print(msg)
   
mensaje('Bienvenido a Python')
mensaje('Mi primer Programa') """

class Sintaxis:
    def usoVariables(self):
        edad, _peso = 50, 70.5
        nombres = 'Daniel Vera'
        Tipo_Sexo = 'M'
        civil = True
        print("civil= {} y su tipo es: {}".format(civil, type(civil))) 
        
ejer1 = Sintaxis() #cinstancia la clase y se crea el objeto1 con todos los atributos y metodos de la clase Sintaxis
ejer1.usoVariables()