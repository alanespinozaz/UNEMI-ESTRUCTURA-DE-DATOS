class Empleado:
    delf__init__(self, nom, car):
        secuencia=0
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.cargo=car
        
    def generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuencia
    def mostar(self):
        print("({})=Nombre:{} ({})=Cargo:{} ".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.descripcion))
        
    