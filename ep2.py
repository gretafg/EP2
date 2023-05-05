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

def preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho):
    posicao = define_posicoes(linha,coluna,orientacao,tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicao)
    else:
        frota[nome_navio]=[posicao]
    return frota

def faz_jogada (tabuleiro, linha, coluna):

    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna]='X'
    else:
        tabuleiro[linha][coluna]='-'
    return tabuleiro

def posiciona_frota(frota):
    grid = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],]

    for linha in range(len(grid)):
        for coordenada in range(len(grid[linha])):
            for infos in frota.values():
                for navio in infos:
                    for ja_posicionado in navio:
                        if ja_posicionado==[linha,coordenada]:
                            grid[linha][coordenada]=1
    return grid
    
def afundados(dici_info, tabuleiro):
    qntd_navios = 0
    for tipo in dici_info.keys():
        infos = dici_info[tipo]
        for i in range(len(infos)):
            navio = infos[i]
            afundado = True 
            for a in range(len(navio)):
                coordenadas = navio[a]
                linha = coordenadas[0]
                coluna = coordenadas[1]
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                    break 
            if afundado:
                qntd_navios += 1
    return qntd_navios

def posicao_valida (dic, linha, coluna, orientacao, tamanho):
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    if posicao not in dic:
        pvalid = True
    else:
        pvalid = False
    return pvalid