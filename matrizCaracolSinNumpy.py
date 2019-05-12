at = [x.split() for x in open("matriz.txt","r").readlines()]

def rotar(lista):
    if len(lista)>=2:
        return list(reversed(map(list, zip(*reversed(lista[::-1])))))
    return lista

def sepLista(lista):
    if lista==[]:
        return []
    return (lista[0] + sepLista((rotar(lista[1:]))))

print sepLista(at)

"""
reversed: cambia el orden del array
zip: convierte en lista y cambia orden dentro de cada renglon
map: convierte el zip en arreglo
list: convierte a lista
El condicional se usa para que cuando no sólo haya un elemento no rote
ya que generaria error
"""
