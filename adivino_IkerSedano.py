def adivino():
    numero=input("Dime un numero del 1 al 10")
    intento=input("intentalo: ")
    while intento!=numero:
        if intento>numero:
            print "Demasiado grande"
        if intento<numero:
            print "Demasiado pequeno"
        intento=input("intentalo de nuevo")
    print "Ahora has acertado"
adivino()
