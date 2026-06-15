def validar_colunas_obrigatorias(colunas_existentes, colunas_obrigatorias):
    existentes = set(colunas_existentes)
    obrigatorias = set(colunas_obrigatorias)
    faltantes = sorted(obrigatorias - existentes)
    return {
        'valido': len(faltantes) == 0,
        'faltantes': faltantes,
    }


def identificar_layout(colunas_existentes, layouts):
    existentes = set(colunas_existentes)
    for nome, obrigatorias in layouts.items():
        if set(obrigatorias).issubset(existentes):
            return nome
    return 'desconhecido'


def exigir_colunas(colunas_existentes, colunas_obrigatorias):
    resultado = validar_colunas_obrigatorias(colunas_existentes, colunas_obrigatorias)
    if not resultado['valido']:
        raise ValueError('Colunas obrigatorias ausentes: ' + str(resultado['faltantes']))
    return True
