# -*- coding: cp1252 -*-
def impuestos():
    print '''Tipos de IVA:
    General
    Reducido
    Superreducido'''
    precio=input("Introduzca el precio del producto: ")
    impuesto=raw_input("Introduzca el IVA a aplicar: ")
    if impuesto=="General":
        iva=0.16
    if impuesto=="Reducido":
        iva=0.07
    if impuesto=="Superreducido":
        iva=0.04
    precio_final=(precio*iva)+precio
    print "Su precio final con IVA aplicado es:" ,precio_final, "€"
impuestos()
                   
    
