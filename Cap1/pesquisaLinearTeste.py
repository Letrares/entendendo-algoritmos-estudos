def pesquisa_linear(lista, item):
    indice = 0 
    
    while indice < len(lista): 

        if lista[indice] == item:
            return indice 
        
        indice = indice + 1
        

    return None


minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_linear(minha_lista, 3))
print(pesquisa_linear(minha_lista, -1))