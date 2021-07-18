clase  Logica :
    def  __init__ ( self , dato ): #datos poner
        yo . __lista = dato         # [2,4,5]
        yo . __estado = Verdadero
        
        
        
    def  par ( yo , número ):
        # numero = int (input ("Ingrese Numero:"))
        
        rec  =  numero  %  2
        # si rec == 0:
        # print ("{} es Par" .format (numero))
        # demás:
        # print ("{} es Impar" .format (numero))
        volver  rec
    
    def  sumaPares ( uno mismo ):
        acu = 0
        para  num  en  sí mismo . __lista :
            si  yo . par ( num ) ==  0 :
               acu  =  acu  +  num
        volver  acu
                
    
    
    def  divisores ( self , numero ):
        acu = 0
        para  divisor  en  rango ( 1 , numero ):
            rec  =  numero  %  divisor
            si  rec  ==  0 :
                acu  =  acu  +  divisor
        # si acu == num:
        # impresión
        volver  acu
    
    def  divisoresNumero ( self , numero ):
        divisores = []
        para  divisor  en  rango ( 1 , numero ):
            rec  =  numero  %  divisor
            si  rec  ==  0 :
                divisores . añadir ( divisor )
        devuelve  divisores
    
                
    
    #entrada proceso salida    
   #numero obtener divisores y sumarlos
    # 6 = 1,2,3 = 6 si es perfecto
    # 8 = 1,2,4 = 7 no es perfecto
                 # acu = 0
        # numero divisor = 1 sumandole uno    
                   
        # 6% 1 = 0 para divisor = 1 hasta numero                      
        # +1 rec = numero% divisor 
        # 6% 2 = 0 acu = acu + divisor si rec = 0
        # +1 acu = acu + divisor 
        # 6% 4 = 0
        # +1
        # 6% 5 = 0
        # +1
              



clase  Ejercicios ( Logica ):
    def  __init__ ( self , numeros , valor ):
       super (). __init__ ( numeros )
       
       
    def  suma ( yo , n1 , n2 ):
        si  super (). par ( n1 ) == 0 :
           return ( n1 + n2 ) * 2
        otra cosa :
           retorno ( n1 + n2 )
    def  resta ( self , n1 , n2 ):
        devuelve  n1 - n2
    
    def  par ( yo , número ):
        rec  =  numero  %  2
        si  rec  ==  0 :
            print ( numero , "Es Par" )
        otra cosa :
            print ( numero , "Es Impar" )
         
       
ejer  =  Ejercicios ([ 2 , 3 , 4 ], 20 )
imprimir ( ejer . par ( 4 ))
imprimir ( ejer . suma ( 4 , 2 ))
# print (ejer .__ lista)



# ejer = Logica ([2,3,5,6,8])
# print (ejer.sumaPares ())

        
        
# ejercicio = Logica ()
# numero = int (input ("Ingrese un Numero:"))
# print (ejercicio.divisoresNumero (numero))
# numeros = (6,28,3,40)
# para num en numeros:
# if ejercicio.perfecto (num) == num:
# print (num, "perfeto")
# demás:
# print (num, "imperfecto")


# num = numero = int (input ("Ingrese un Numero:"))
# numeros = [1,3,8,4,5,10]
# pares = []
# impares = {}
# para num en numeros: 
# if ejercicio.par (num) == 0: #! se coloca para buscar impares
# pares.append (num)
# print (num, "par")
# demás:
# impares [num] = "Impar"
        
# imprimir (pares)
# print (impares)
    



       
        
               # Problema: par o impar
    # entrada proceso salida
    # numero calculo divisible 2 par o impar
    
    # 4 4% 2 = 0
    # 5 5% 2 = 1
    # 8
    
    # rec = numero% 2
    # si rec = 0
    # escribir "par"
    # Sino
    # escribir "impar"  
    # num 
    # 4/2 
    # rec (0) 2 cos 