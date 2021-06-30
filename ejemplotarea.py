# "" "1. Determinar la cantidad de dinero que tuvo un trabajador por concepto de las horas extras trabajadas en una empresa, 
#  sabiendo que cuando las horas de trabajo exceden de 40, el resto se consideran horas extras y que están paganas al doble de una hora normal cuando no exceden de 8;  
# si las horas extras exceden de 8 se pagan las primeras 8 al doble de lo que se paga por una hora normal y el resto al triple. "" "
 
# "" "Calcular el factorial de N números enteros leídos de teclado.
# El problema consistirá en realizar una estructura de N iteraciones aplicando el factorial de un número.
# El pseudocódigo es el siguiente: "" "

clase  Tarea :
     def  __init__ ( yo ):
         aprobar
     def  calculoPago ( self ):
        ht , él , het  =  0 , 0 , 0 
        ph ,   phe , pt  =  0 , 0 , 0
        
        ht  =  int ( input ( "Ingrese horas trabajadas:" ))
        ph  =  float ( input ( "Ingrese valor hora:" ))
        if  ht  >  40 : # debe ser 41 para calcular las horas extras
          print ( "En proceso de calculo ....." )
          él  =  altura  -  40
          si  él  >  8 :
             het  =  él  -  8
             él = 8
             phe  =  ph  *  2  *  he  +  ph  *  3  *  het
          otra cosa :
               phe  =  ph  *  2  *  él 
          pt  =  ph * 40  + phe   
          
        otra cosa :
            pt  =  ph  *  ht
            
        print ( "El pago total de horas trabajadas es:" , pt )
        


                 # núm 2 = 2 * 1 = 2



     def  factorial ( uno mismo ):
        n  =  int ( input ( "Ingrese cantidad de numeros:" ))    
        para   i  en el  rango ( n ):    
            numero  =  int ( input ( "Ingrese numero:" ))
            # calculo del factorial
            hecho = 1
            # mientras num> 0:
            # acu = acu * num
            # num = num -1
            para   num  en  rango ( numero , 0 , - 1 ):
                   hecho = hecho * num  
        print ( "factorial del numero: {} es: {}" . format ( numero , fact ))
        
        
tarea  =  Tarea ()
# tarea.calculoPago ()
tarea . factorial ()