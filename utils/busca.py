def busca_binaria(lista, codigo):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        atual = lista[meio].codigo
        if atual == codigo:
            return meio
        elif atual < codigo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1