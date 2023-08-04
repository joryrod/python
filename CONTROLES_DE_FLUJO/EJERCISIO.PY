#crear una funcion que reciba como parametro una lista->lista
#y retorne una lista d eobjetos que tendra las carcateristicas de cada 
#elemento del array->lista
## la lista va tener un objeto por cada elemento, 
#[{longitud:6, nombre:"bosque",posicion:0 },{},{}]


lista=["gato","perro","canario"]
def elementos(lista):
   lista_elementos=[]
   for indice,valor in enumerate(lista):
       objeto={
           "longitud":len(valor),
           "objeto_valor":valor,
           "objeto_posicion":indice
        }
       lista_elementos.append(objeto)
   return lista_elementos
lista_elementos=elementos(lista)
print (lista_elementos)



#crear una funcion que reciba como parametro dos listas y retorne un array de objetos
#con las siguientes caracteristicas
#[{nombre:jory,edad:50,completo:jory 50},
# {nombre:orlando, edad:15, completo:orlando 15},
# {nombre:yadira, edad:10, completo: yadira 10}]

nombre=['jory','orlando','yadira']
edad=[50,15,10]
completo=nombre+edad
def alumnos(nombre,edad):
    alumnos=[]
    for i in range(len(nombre)):
        
        objeto={
                'nombre':nombre[i],
                'edades':edad[i],
                'completo':f"{nombre[i]} {edad[i]}"
        }
        alumnos.append(objeto)
    return alumnos
mis_alumnos=alumnos(nombre,edad)
print(mis_alumnos)