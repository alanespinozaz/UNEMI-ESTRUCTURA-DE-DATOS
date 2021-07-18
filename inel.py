clase  Buscador :
    def  __init__ ( self , dato ):
        yo . lista = dato
        
        
    def  recorrerElemento ( yo ):
        para  ele  en  sí mismo . lista :    # [:: - 1] / para colocarlo al reves
            print ( ele , end = "" )
        para  ele  en  sí mismo . lista [:: - 1 ]:
            print ( ele , end = "" )    
            
        imprimir ()     
        para  pos , ele  en  enumerate ( self . lista ):
            print ( "[{}] = {}" . formato ( pos , ele ))
        imprimir ()    
        
        para  pos  en  gama ( len ( auto . de Lista ) - 1 , 0 , - 1 ):
            print ( "[{}] = {}" . formato ( pos , self . lista [ pos ]))     
    
    
    def  buscar ( self , buscado ):
        encontrado = Falso
        para  pos , ele  en  enumerate ( self . lista ):
             if  ele == buscado :
                 encontrado = Verdadero
                 romper  # rompe el para
                 
         
        si se  encuentra :    devolver  pos
        else :             return  - 1 
        
    def  ordenarAsc ( yo ):
        para  pos  en  rango ( 0 , len ( auto . de Lista ) - 1 ):
            para  sig  en  gama ( pos + 1 , len ( auto . Lista )):
                si  yo . lista [ pos ] >  self . lista [ sig ]:
                    aux  =  self . lista [ pos ]
                    yo . lista [ pos ] = self . lista [ sig ]
                    yo . lista [ sig ] = aux
        
    def  ordenarDes ( self ):
        para  pos  en  rango ( 0 , len ( auto . de Lista ) - 1 ):
            para  sig  en  gama ( pos + 1 , len ( auto . Lista )):
                si  yo . lista [ pos ] <  self . lista [ sig ]:
                    aux  =  self . lista [ pos ]
                    yo . lista [ pos ] = self . lista [ sig ]
                    yo . lista [ sig ] = aux           
            
             
             
     
    def  primer ( uno mismo ):
        volver a  sí mismo . lista [ 0 ]
    
    def  primerElemento ( self ):
        primero = self . lista [ 0 ]
        yo . lista  =  self . lista [ 1 :]
        volver  primero
    
    def  primerElemento2 ( self ):
        primero = self . lista [ 0 ]
        auxiliar = []
        para  pos  en  gama ( 1 , len ( auto . Lista )):
            auxiliar . append ( auto . Lista [ pos ])
        yo . lista = auxiliar
        volver  primero     
    
    
    def  ultimo ( yo ):
        volver a  sí mismo . lista [ - 1 ]
    
    def  ultimoElemento ( yo ):
        ultimo = self . lista [ - 1 ]
        yo . lista  =  self . lista [: - 1 ]
        volver  ultimo  

    def  ultimoElemento2 ( yo ):
        ultimo = self . lista [ - 1 ]
        auxiliar = []
        para  pos  en  rango ( 0 , len ( auto . de Lista ) - 1 ):
            auxiliar . append ( auto . Lista [ pos ])
        yo . lista = auxiliar
        volver  ultimo
          
          
          
    def  insertar ( self , num ):
        yo . ordenarAsc ()
        auxiliar = []
        para  pos , ele  en  enumerate ( self . lista ):
            si  num  <  ele :
                auxiliar . añadir ( num )
                rotura
        
        yo . lista = self . lista [ 0 : pos ] + auxiliar + self . lista [ pos :]
        
        
    def  insertar2 ( self , num ):
        yo . ordenarAsc ()
        auxlista = []
        para  pos , ele  en  enumerate ( self . lista ):
            si  num  <  ele :
                rotura
        para  i  en  rango ( pos ):
            auxlista . append ( auto . Lista [ i ])
        auxlista . añadir ( num )
        para  j  en  rango ( pos , len ( auto . Lista )):
            auxlista . append ( auto . Lista [ j ])
        yo . lista = auxlista
            
        # self.lista = self.lista [0: pos] + auxiliar + self.lista [pos:]
          
          
          
    def  insertarOrden ( self , num ):
        yo . lista . añadir ( num )
        yo . ordenarAsc ()
          
   
    def  eliminar ( self , num ):
        enc = Falso
        para  pos , ele  en  enumerate ( self . lista ):
            si  num  ==  ele :  
                enc = Verdadero
                rotura
        if  enc : self . lista = self . lista [ 0 : pos ] + self . lista [ pos + 1 :]
        retorno  enc    
             
             
             
             
             
             
datos  = [ 2 , 3 , 8 , 10 ] # = [2,3,5,8,10] #Ejecutar

# # insertar = 5 = [2,3,8,10]

#bus = Buscador (datos)
# # num = 18
# datos.sort () # haciendo pruebas con el sort ascendentes / sorted
#print (datos) # para que me imprima la lista ordenada
#bus = Buscador (datos) #Ejecutar

# if bus.eliminar (2) == True: print ("El numero que coloco se elimino de la lista", bus.lista) #Ejecutar
# else: print ("El numero agregado no se encuentra en la lista, por ese motivo no se procede a eliminar") #Ejecutar

# print (bus.ultimoElemento2 (), bus.lista) #Ejecutar





#print (datos)
# bus = Buscador (datos)
# print (bus.lista)
# bus.ordenarAsc ()
# print (bus.lista)
# bus.ordenarDes ()
# print (bus.lista)



# buscado = 1

# datos = "Hola"
# 0 1 2 3 4        

# bus.recorrerElemento ()
# valor = 1
# resp = bus.buscar (valor)
# if resp! = - 1: print ("el numero: {} se encuentra en la posicion: [{}] de la lista: {}". format (valor, resp, bus.lista))
# else: print ("el numero: {} no se encuentra en la lista: {}". format (valor, bus.lista))

# numerosbuscados = (2,4,6,1)
# respuestas = {}
# por valor en numerosbuscados:
# resp = bus.buscar (valor)
# if resp! = - 1: respuestas [valor] = resp
# print (respuestas)


                                                           
                                            
                                            #Ejemplo 



# lista = [2,4,8,5,10,7,8,9]
# # 0 1 2 3 4 5 6 7

# x = lista [2]
# lista1 = lista [1:]
# lista2 = lista [1: 3]
# lista3 = lista [0: -1]
# lista4 = lista [+1]
# lista5 = lista [1: -1]
# lista6 = lista [: - 1]

# para pos en rango (len (lista) -1):
# print ("Primer para", pos, lista [pos])
# para j en el rango (pos + 1, len (lista)):
# print ("Segundo para", lista [j])
# input ("presione alguna tecla para continuar ....")