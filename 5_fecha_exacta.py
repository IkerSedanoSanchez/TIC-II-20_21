
def fecha():
    meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    dia=input("Introduzca un numero para el dia (del 1 al 31): ")
    while dia<1 or dia>31:
        print "Del 1 al 31"
        dia=input("Introduzca un numero para el dia (del 1 al 31): ")
    numero2=input("Introduzca un numero para el mes (del 1 al 12): ")
    while numero2<1 or numero2>12:
        print "Del 1 al 12"
        numero2=input("Introduzca un numero para el mes (del 1 al 12): ")
    mes=meses[numero2-1]
    ano=input("Introduzca un numero para el ano: " )
    if ano<0 :
        print "Su fecha escogida es: ",dia,"de",mes,"del",ano*-1,"aC"
    if ano>0 or ano==0:
        print "Su fecha escogida es: ",dia,"de",mes,"del",ano,"dC"
    
fecha()
    
    
