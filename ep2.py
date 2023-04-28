def define_posicoes (linha, coluna, orientacao, tamanho):
    posicao = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            lista = [linha+i,coluna]

        if orientacao == 'horizontal':
            lista = [linha,coluna+i]

        posicao.append(lista)
    return posicao