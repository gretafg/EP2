#Função que posiciona o navio no grid (retorna suas coordenadas com [linha,coluna])
def define_posicoes (linha, coluna, orientacao, tamanho):
    posicao = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            lista = [linha+i,coluna]

        if orientacao == 'horizontal':
            lista = [linha,coluna+i]

        posicao.append(lista)
    return posicao

#Função que faz a jogada (define 'X' quando atingir o barco e '-' quando for água)
def faz_jogada (tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna]='X'
    else:
        tabuleiro[linha][coluna]='-'
    return tabuleiro