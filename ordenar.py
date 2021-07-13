clase  Buscador :
    def  __init__ ( self , dato ):
        yo . lista = dato
        
        
    def  recorrerElemento ( yo ):
        para  ele  en  sí mismo . lista :    # [:: - 1] / para colocarlo al reves
            print ( ele , end = "" )
        para  ele  en  sí mismo . lista [:: - 1 ]:
            print ( ele , end = "" )    
            
        imprimir ()     
        para  POS , ele  en  enumerate ( auto . Lista ):
            print ( "[{}] = {}" . formato ( pos , ele ))
        imprimir ()    
        
        para  pos  en  gama ( len ( auto . de Lista ) - 1 , 0 , - 1 ):
            print ( "[{}] = {}" . formato ( pos , self . lista [ pos ]))     
    
    
    def  buscar ( self , buscado ):
        encontrado = Falso
        para  POS , ele  en  enumerate ( auto . Lista ):
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
        aprobar
          
             
datos  = [ 10 , 15 , 18 , 20 , 30 ]

num = 18
# datos.sort ()
imprimir ( datos )
bus  =  Buscador ( datos )
imprimir ( bus . ultimoElemento2 (), bus . lista )





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