def contrasena_2():
    nombre=raw_input("Nombre: ")
    apellido=raw_input("Apellido: ")
    contrasena=nombre[-3:]+ apellido[-3:]
    print("Contrasena: ",contrasena)

contrasena_2()
