class For:
    def __init__(self):
        pass
    
    def usoFor(self):
        # ciclo repetitivo automatico se ejecuta desde un valor inicial hasta alcanzar el valor final
        nombre = "Daniel"
        datos=["Daniel",50,True]
        # pos      0     1   2
        numeros=(2,5,6,4,1)
        docentes = {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
        listaNotas = [(30,40),(20,40,50),(50,40)]
        listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"Yady","final":60},{"nombre":"Danny","final":90}]
        #! range ([inicio=0],limite,[inc/dec=1]). Genera un rango de valores desde un valor inicial a un valor final
        #* for con range() para generar valores desde - hasta o for con colecciones para para recorrer elem x elem
        for i in range(5): #! (0,1,2,3,4)
            print("i={}".format(i))
        for i in range(2,5): #! (2,3,4)
            print("i={}".format(i))
        for i in range(10,2,-2): #! (10,8,6,4)
            print("i={}".format(i))
bucle = For()
bucle.usoFor()
print(bucle.numero)