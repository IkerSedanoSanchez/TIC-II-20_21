def multiplicacion():
    numero1=input ("Introduzca un numero distinto de 0: ") 
    while numero1==0 :
        print "Distinto de cero"
        numero1=input ("Introduzca un numero distinto de 0: ")
    numero2=input ("Introduzca un numero distinto de 0: ")
    while numero2==0 :
        print "Distinto de cero"
        numero2=input ("Introduzca un numero distinto de 0: ")
    numero3=input ("Introduzca un numero distinto de 0: ")
    while numero3==0 :
        print "Distinto de cero"
        numero3=input ("Introduzca un numero distinto de 0: ")
    numero4=input ("Introduzca un numero distinto de 0: ")
    while numero4==0 :
        print "Distinto de cero"
        numero4=input ("Introduzca un numero distinto de 0: ")
    numero_final=(numero1*numero2*numero3*numero4)
    print "Su numero multiplicado es: ",numero_final
multiplicacion()
