def preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho):
    posicao = define_posicoes(linha,coluna,orientacao,tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicao)
    else:
        frota[nome_navio]=[posicao]
    return frota

def define_posicoes(linha,coluna,orientacao,tamanho):
    resp = []
    for i in range(tamanho):
        if orientacao=='vertical':
            lista = [linha+i,coluna]
        elif orientacao=='horizontal':
            lista = [linha,coluna+i]
        else:
            lista = [linha,coluna]
        resp.append(lista)
    return resp

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

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna]==1:
        tabuleiro[linha][coluna]='X'
    else:
        tabuleiro[linha][coluna]='-'
    return tabuleiro

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

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

nomes = ['porta-aviões','navio-tanque','navio-tanque','contratorpedeiro','contratorpedeiro','contratorpedeiro','submarino','submarino','submarino','submarino']
tamanhos = {'porta-aviões':4,'navio-tanque':3,'contratorpedeiro':2,'submarino':1}
valores = [0,1,2,3,4,5,6,7,8,9,'1','2','3','4','5','6','7','8','9','0']
i = 0
while i != len(nomes):
    nome = nomes[i]
    tamanho = tamanhos[nome]
    print('Insira as informações referentes ao navio {} que possui tamanho {}' .format(nome,tamanho))
    linha = int(input('Insira aqui a linha'))
    coluna = int(input('Insira aqui a coluna'))
    if linha<0 or linha>9 or coluna<0 or coluna>9:
        print('Esta posição não está válida!')
    else:
        orientacao = 'vertical'
        if tamanho!=1:
            orientacao = int(input('Qual a orientação'))
            if orientacao!=1 and orientacao!=2:
                orientacao = 'invalida'
            elif orientacao==1:
                orientacao='vertical'
            elif orientacao==2:
                orientacao = 'horizontal'

        if orientacao!='invalida':
            valida = posicao_valida(frota,linha,coluna,orientacao,tamanho)
            if valida==False:
                print('Esta posição não está válida!')
            else:
                frota=preenche_frota(frota,nome,linha,coluna,orientacao,tamanho)
                i+=1
        else:
            print('Esta posição não está válida!')

print(frota)