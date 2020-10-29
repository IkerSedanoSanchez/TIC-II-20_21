def letra_funcion():
    print """
    ***MENU***
    S de suma
    R de resta
    M de multiplicacion
    D de division"""
    interruptora=1
    while(interruptora==1):
        numero=input ("Introcuzca el primer numero: ")
        numero2=input ("Introduzca el segundo numero: ")    
        funcion=raw_input ("Introduzca una letra para definir la operacion: ")
        if funcion=="S":
            operacion=numero+numero2
            interruptora=0
            print numero,"+",numero2,"=",operacion
        if funcion=="R":
            operacion=numero-numero2
            interruptora=0
            print numero,"-",numero2,"=",operacion
        if funcion=="M":
            operacion=numero*numero2
            interruptora=0
            print numero,"*",numero2,"=",operacion
        if funcion=="D":
            if (numero2!=0):
                interruptora=0
                operacion=numero/numero2
                print numero,"/",numero2,"=",operacion
            else:
                print "0 en el divisor no computa, brrr,introduce otra operacion, brrr"
                interruptora=1
              
     
letra_funcion()
