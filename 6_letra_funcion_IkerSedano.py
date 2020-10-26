def letra_funcion():
    print """
    S de suma
    R de resta
    M de multiplicacion"
    D de division"""
    numero=input ("Introcuzca un numero: ")
    numero2=input ("Introduzca un numero: ")
    funcion=raw_input ("Introduzca una letra para definir la operacion: ")
    if funcion=="S":
        operacion=numero+numero2
        print numero,"+",numero2,"=",operacion
    if funcion=="R":
        operacion=numero-numero2
        print numero,"-",numero2,"=",operacion
    if funcion=="M":
        operacion=numero*numero2
        print numero,"*",numero2,"=",operacion
    if funcion=="D":
        operacion=numero/numero2
        print numero,"/",numero2,"=",operacion
    
letra_funcion()
