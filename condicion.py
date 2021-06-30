# "" "Construir un algoritmo tal, que dado como dato la calificación de un alumno en un examen, escriba
# DEFINICIÓN DEL PROBLEMA
# El mismo enunciado.
# ANÁLISIS DEL PROBLEMA
# Salidas: mensaje de aprobado si se cumple la condición.
# Entradas: calificación
# Datos adicionales: un alumno aprueba si la calificación es mayor o igual que 7. "" "

clase  Condicion :

   def  __init__ ( yo ):
       aprobar
       
   def  NF ( propio ):
        NT  =  float ( input ( "Ingrese su Nota final:" ))
        si  NT  > =  7 :
            print ( "Su nota final es {}, Felicitaciones usted ha aprobado el curso" . formato ( NT ))   
        otra cosa :
            print ( "Usted ha Reprobado el Curso, con la siguiente nota {}" . formato ( NT ))
               
condi1  =  Condicion ()
condi1 . NF ()  