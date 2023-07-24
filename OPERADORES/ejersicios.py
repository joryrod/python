edad=int(input("cuantosaños tiene?: "))
if edad<18:
    print("es cana manito")
elif edad>18 and edad<40:
    print("ya comela bandida")
else:
    print("ya se nos paso de madura")


###segundo ejercicio
dni=input("escriba su numero de DNI: ")
caracteres=len(dni)
if caracteres==8:
    nombre=input("nombre: ")
    print(f"""
====================================
muy bien su DNI es correcto {nombre}
====================================
""")
elif caracteres!=8:
    print(f"""
===============================
ese numero de DNI es invalido
===============================
""")