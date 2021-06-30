# importar la clase cargo del archivo cargo.py (11)
de  carga de  importación  Carga

clase  Empleado :
    secuencia = 0

    def  __init__ ( self , nom , car ):
        yo . codigo = yo . generarCodigo ()
        yo . nombre = nom
        yo . cargo = coche
        
    def  generarCodigo ( yo ):
        Empleado . secuencia = Empleado . secuencia + 1
        volver  Empleado . secuencia
    def  mostrar ( yo ):
        print ( "({}) - Nombre: {} ({}) - Cargo: {}" . formato ( self . codigo , self . nombre , self . cargo . codigo , self . cargo . descripcion ))

cargo1  =  Cargo ( "Docente" )
cargo2  =  Cargo ( "Director" )

emp1  =  Empleado ( "Daniel" , cargo1 )
emp1 . mostrar ()
emp2  =  Empleado ( "Daniel" , cargo2 )
emp2 . mostrar ()