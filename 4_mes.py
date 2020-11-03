def nombre_mes():
    meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    numero=input("Introduce un numero del 1 al 12: ")
    while numero<1 or numero>12:
        print "Del 1 al 12 crack"
        numero=input("Introduce un numero del 1 al 12: ")
    mes=meses[numero-1]
    print "El mes escogido es",mes
nombre_mes()
