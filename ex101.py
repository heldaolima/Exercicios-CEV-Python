
def voto(nasc):
    """
    -> Analisa a idade da pessoa para determinar a sua situação como eleitora.
    :param nasc: ano de nascimento da pessoa
    :return: a situação [NÃO VOTA, VOTO OBRIGATÓRIO, VOTO OPCIONAL]
    """
    from datetime import datetime
    hoje = datetime.today().year
    idade = hoje - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print('---------------------')
nasc = int(input('Ano de nascimento: '))
print(voto(nasc))
