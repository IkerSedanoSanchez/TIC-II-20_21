def dia_semana():
    numero=input("Introduzca un numero del 1 al 7: ")
    while numero<1 or numero>7 :
        print "Del 1 al 7, atontao"
        numero=input("Introduzca un numero del 1 al 7: ")
    dias=["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
    dia=dias[numero-1]
    print "El dia que ha escogido es el", dia
dia_semana()

