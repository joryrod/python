## lista=[]
## print(lista)
## primerDato=input("ingresaunafruta: ")
## lista.append(primerDato)
## print(lista)
## segundoDato=input("ingrese una segunda fruta: ")
## lista.append(segundoDato)
## print(lista)


# lista=[]
# datos=(input("ingrese un numero ( {si} parafinalizar): "))
# while datos!="si":
#     lista.append(datos)
#     datos=(input("ingrese un numero ( {si} parafinalizar): "))
# print(lista)



lista=[]
while True:
    pedirDato=input("ingreseun dato: ")
    if pedirDato=="si":
        break
    lista.append(pedirDato)
print(lista)

