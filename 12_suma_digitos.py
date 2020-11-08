def suma_digitos():
    numero=input("Introduzca un numero (4 cifras maximo): ")
    numero1=numero/1000
    numero12=numero%1000
    numero2=numero12/100
    numero22=numero12%100
    numero3=numero22/10
    numero4=numero22%10
    print "Su suma de digitos es:",numero1,"+",numero2,"+",numero3,"+",numero4,"=",(numero1+numero2+numero3+numero4)
suma_digitos()
    
