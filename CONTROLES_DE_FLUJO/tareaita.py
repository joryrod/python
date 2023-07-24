# galeria_productos = {
#     "001": {"nombre": "CAMIZA", "precio": 30.00},
#     "002": {"nombre": "CINTURON", "precio": 15.00},
#     "003": {"nombre": "ZAPATOS", "precio": 90.00},
#     "004": {"nombre": "PANTALON", "precio": 60.00},
#     "005": {"nombre": "CALCETINES", "precio": 5.00},
#     "006": {"nombre": "FALDAS", "precio": 40.00},
#     "007": {"nombre": "GORRAS", "precio": 10.00},
#     "008": {"nombre": "SUETER", "precio": 50.00},
#     "009": {"nombre": "CORBATA", "precio": 5.00},
#     "010": {"nombre": "CHAQUETA", "precio": 100.00},
# }

# def calcular_total(productos_comprados):
#     total = 0.0
#     for codigo, unidades in productos_comprados.items():
#         if codigo in galeria_productos:
#             precio_unitario = galeria_productos[codigo]["precio"]
#             total += precio_unitario * unidades
#     return total

# def main():
#     print("Bienvenido a la tienda")
#     print("Galería de productos:")
#     for codigo, producto in galeria_productos.items():
#         print(f"{codigo}: {producto['nombre']} - Precio: {producto['precio']}")

#     productos_comprados = {}
#     while True:
#         codigo = input("Ingrese el código del producto que desea comprar (o 'fin' para terminar): ")
#         if codigo.lower() == "fin":
#             break

#         if codigo not in galeria_productos:
#             print("Código inválido. Intente nuevamente.")
#             continue

#         unidades = int(input("Ingrese la cantidad de unidades que desea comprar: "))
#         if unidades <= 0:
#             print("La cantidad debe ser mayor que cero. Intente nuevamente.")
#             continue

#         if codigo in productos_comprados:
#             productos_comprados[codigo] += unidades
#         else:
#             productos_comprados[codigo] = unidades

#     total_a_pagar = calcular_total(productos_comprados)

#     print("\nFactura:")
#     for codigo, unidades in productos_comprados.items():
#         producto = galeria_productos[codigo]
#         subtotal = producto["precio"] * unidades
#         print(f"{producto['nombre']} - {producto['precio']} x {unidades} = {subtotal}")

#     print(f"Total a pagar: {total_a_pagar:.2f}")

# if __name__ == "__main__":
#     main()


# print("""
#             BIENVENIDO... A NUETRA TIENDA
#         (\_ /)
#         ( °-°)
#         /> REALIZA TU COMPRA ;)
# """)
# print ("""
#     ------------------------------------
#     ELIJA EL PRODUCTO QUE VA A COMPRAR: 
#     ------------------------------------
#        """)

# print ("PRODUCTO\t\t\tCODIGO\t\t\tPRECIO")
# print (f"""
# CAMISA........................... 1 .................. S/. 35.00
# CINTURON......................... 2 .................. S/. 10.00
# ZAPATOS.......................... 3 .................. S/. 50.00
# PANTALON......................... 4 .................. S/. 40.00
# CALCETINES....................... 5 .................. S/. 6.00
# FALDAS........................... 6 .................. S/. 45.00
# GORRAS........................... 7 .................. S/. 20.00
# SUETER........................... 8 .................. S/. 70.00
# CORBATA.......................... 9 .................. S/. 15.00
# CHAQUETA......................... 10 ................. S/. 145.00
#        """)
# cuenta=[]
# precios = [35,10,50,40,6,45,20,70,15,145]

# comprando= 0

# while comprando == 0:
#     codigo = int(input("INGRESE EL CODIGO DEL ARTICULO EN COMPRA: "))
#     print("EL PRECIO ES: S/.", precios[codigo-1])
#     cantidad =int(input("INGRESE LA CANTIDAD DE ARTICULOS EN COMPRA: "))
#     cuenta.append((precios[codigo-1])*cantidad)
#     comprando=int(input("PARA AGREAGAR OTRO ARTICULO 0 PARA SALIR 1: "))

# precio_total= 0

# for precios in cuenta :
#     precio_total = precio_total + int(precios) 
# print("==============================================")
# print("TOTAL A PAGAR ES: S/."+ str(precio_total))
# print("==============================================")



print("CATEGORIA\t\t PRECIO\t\t\tCODIGO\t\t RECARGO / DIA DE ATRASO")
print("Favoritos\t\t S/. 8.90\t\t 1\t\t S/. 1.80")
print("Nuevos\t\t\t S/. 10.77\t\t 2\t\t S/. 2.69")
print("Estrenos\t\t S/. 12.57\t\t 3\t\t S/. 3.59")
print("Super estrenos\t\t S/. 14.36\t\t 4\t\t S/. 5.39")

codigo = int(input("INGRESE EL CODIGO DE LA CATEGORIA DE UNA PELICULA: "))
dias = int(input("INGRESE EL NUMERO DE DIAS DE ATRASO EN LA DEVOLUCION: "))
codigo in range(1,4)

if codigo > 4:
    print("""ERROR...
          EL CODIGO INGRESADO ES INVALIDO...
          INGRESA UN CODIGO VALIDO :)
          """)
else:
    if codigo==1:
        retraso = (8.90 + (dias * 1.80))
        print("EL TOTAL A PAGAR ES: S/. ",retraso," SOLES")
    elif codigo==2:
        retraso = (10.77 + (dias * 2.69))
        print("EL TOTAL A PAGAR ES: S/. ",retraso," SOLES")
    elif codigo==3:
        retraso = (12.57 + (dias * 3.59))
        print("EL TOTAL A PAGAR ES: S/. ",retraso," SOLES")
        
    else:
        retraso = (14.36 + (dias * 5.39))
        print("EL TOTAL A PAGAR ES: S/. ",retraso," SOLES")