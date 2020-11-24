def notas(*n, sit=False):
    """
    -> Analisa várias notas de um aluno e calcula a sua situação
    :param n: notas do aluno (aceita várias)
    :param sit: se mostra ou não a situação do aluno (opcional)
    :return: dicionário com as informações
    """
    dicio = {}
    dicio['quantidade'] = len(n)
    dicio['maior'] = max(n)
    dicio['menor'] = min(n)
    dicio['media'] = sum(n) / len(n)
    if sit is True:
        if dicio['media'] < 6:
            dicio['situação'] = 'RUIM'
        elif 6 < dicio['media'] < 7:
            dicio['situação'] = 'RAZOÁVEL'
        elif dicio['media'] >= 7:
            dicio['situação'] = 'BOA'
    print('-'*40)
    return dicio


resp = notas(4, 6.5,10, 7.8, sit=False)
print(resp)
