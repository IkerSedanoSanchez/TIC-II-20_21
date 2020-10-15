import random

def adivino_2():
    maxn=10
    numero=random.randint(1,maxn)
    intento=input("Intentalo: ")
    while intento!=numero:
        if intento>numero:
            print "Demasiado grande"
        if intento<numero:
            print "Demasiado pequeno"
        intento=input("Intentalo de nuevo: ")
    print "Ahora has acertado GG well played"
adivino_2()
