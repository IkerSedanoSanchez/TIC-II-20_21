'''Escribe un programa que genere contrasena'''
def contrasena():
    nombre=raw_input("Introduce el nombre: ")
    apellido=raw_input("Introcude el apellido: ")
    print nombre,apellido,"eres el impostor?"
    print "Las tres letras inicales",3*nombre+2*apellido
   
contrasena()
