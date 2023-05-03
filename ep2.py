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

#Função que valida se o navio cabe nos espaços dependendo do seu tamanho e orientação
def posicao_valida(infos_navios,linha,coluna,orientacao,tamanho):
    resp = True
    posicoes = define_posicoes(linha,coluna,orientacao,tamanho)
    for i in range(len(posicoes)):
        coordenadas = posicoes[i]
        l = coordenadas[0]
        c = coordenadas[1]
        if l>=10 or c>=10:
            return False
        for tipo in infos_navios.values():
            for b in range(len(tipo)):
                navio = tipo[b]
                for a in range(len(navio)):
                    if navio[a]==coordenadas:
                        return False
    return resp