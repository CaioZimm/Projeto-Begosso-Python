def ler_codigo(mensagem="Código da cidade: "):
    entrada = input(mensagem).strip()

    if not entrada:
        return False, "Nenhum código digitado. Operação cancelada."

    try:
        codigo = int(entrada)
        return True, codigo
    except ValueError:
        return False, "Código inválido. Digite um número inteiro."
