clase  para :
    def  __init__ ( self , lim = 12 ):
        yo . n = lim
    
    def  usoFor ( self ):
        # ciclo repetitivo automatico (de incrementos o decrementos) que se ejecuta hasta alcanzar (el valor final) un valor final.
       nombre  =  "Daniel"
       #pos 012345
       datos = [ "Daniel" , 50 , verdadero ]
       #pos 0 1 2 
       numeros = ( 2 , 5 , 6 , 4 , 1 )
       docente  = { 'nombre' : 'Daniel' , 'edad' : 50 , 'fac' : 'faci' }
       listaNotas  = [( 30 , 40 ), ( 20 , 40 , 50 ), ( 50 , 40 )]
       listaAlumnos  = [{ "nombre" : "Erick" , "final" : 70 }, { "nombre" : "Yadi" , "final" : 60 }, { "nombre" : "Danny" , "final" : 90 } ]
        # rango ([inicio = 0], limite, [inc / dec = 0]). Generea un rango de valores desde un valor inicial a un valor final
        # for con range () para generar valores o for con colecciones para recorrer elementos por elementos de la coleecione
        #for i en el rango (5): #genera valores (0,1,2,3,4)
        # print ("i = {}". formato (i))
        #for i en rango (2,5): #genera valores (2,3,4)
        # print ("i = {}". formato (i))
        #for i en rango (3, self.n, 3): #genera valores (3,6,9)
        # print ("i = {}". formato (i), end = "")
        # long = len (nombre)
        # para pos en rango (largo): # (0,1,2,3,4,5)
        # print (nombre [pos], end = "")
        # long = len (datos)
        # para pos en rango (largo): # (0,1,2,3,4,5)
        # print (datos [pos], end = "")
        # para pos, elem en enumerate (nombre): # ((0, "daniel"), (1,50), (2, true))
        # print (pos, "", elem)
        # para elem en datos: # 'danuiel'.50, verdadero
        # imprimir (elem)
        # para num en numeros: print (num)
        # Daniel
        # 012345
        # para pos, elem en enumerate (nombre): #
        # si pos% 2 == 0 y pos! = 0:
        # imprimir (elem)
        # docente = {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
        # para clave, valor en docente.items ():
        # print (clave, valor, end = "")
        # lista = [2,4,5,5]
        # acu = 0
        # para ele en lista:
        # acu = acu + ele
        # imprimir (acu)
        # acu = 0
        # listaAlumnos = [{"nombre": "Erick", "final": 70}, {"nombre": "Yadi", "final": 60}, {"nombre": "Danny", "final": 90 }]   
        # para alumnos en listaAlumnos:
        # print (alumnos)
        # acu = acu + alumnos ["final"]
        # imprimir (acu)
        # acu = 0
        # cont = 0
        # listaAlumnos = [{"nombre": "Erick", "final": 70}, {"nombre": "Yadi", "final": 60}, {"nombre": "Danny", "final": 90 }]   
        # para alumnos en listaAlumnos:
        # cont + = 1
        # para c, v en alumnos.items ():
        # imprimir (c, v)
        # si c == "final":
        # acu = acu + v
        # #print (acu, acu / len (listaAlumnos))
        # imprimir (acu, acu / cont)
       
       listaNotas  = [( 30 , 40 ), ( 20 , 40 , 50 ), ( 50 , 40 , 10 , 45 ), ( 5 , 15 )]
       acu , cont = 0 , 0
       para  notas  en  listaNotas :
           imprimir ( notas )
           acumParcial = 0
           para  nota  en  notas :
               #print (nota)
               # acu + = nota
               acumParcial + = nota
               # cont + = 1
           cont + =  len ( notas )
           acu + =  acumParcial
           print ( acumParcial , acumParcial / len ( notas ))
       imprimir ( acu , acu / cont )
       
bucle1  =  Para ()
bucle1 . usoFor ()

# bucle2 = Para (12)
# bucle2.usoFor () 
#print (bucle.numero)