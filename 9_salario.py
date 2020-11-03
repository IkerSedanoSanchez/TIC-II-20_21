# -*- coding: cp1252 -*-
def salario():
    horas=input("Introduzca las horas que trabaja semanalmente: ")
    horas_extra=(horas-40)
    if horas_extra<0:
        horas_extra=0
    horas_ordinarias=(horas-horas_extra)
    salario=(horas_ordinarias*30)+(horas_extra*45)
    print "Su salario semanal es: ",salario,"€"
salario()
