import random
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

def faz_jogada(tabuleiro, linha, coluna):

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

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

nomes = ['porta-aviões','navio-tanque','navio-tanque','contratorpedeiro','contratorpedeiro','contratorpedeiro','submarino','submarino','submarino','submarino']
tamanhos = {'porta-aviões':4,'navio-tanque':3,'contratorpedeiro':2,'submarino':1}
i = 0
while i != len(nomes):
    nome = nomes[i]
    tamanho = tamanhos[nome]
    print('Insira as informações referentes ao navio {} que possui tamanho {}' .format(nome,tamanho))
    linha = int(input('Insira aqui a linha'))
    coluna = int(input('Insira aqui a coluna'))
    orientacao = 1
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

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)
ataques_jogador=[]
ataques_oponente = []
jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    jogada_jogador=True
    while jogada_jogador:
        l_ataque = int(input('Qual linha deseja atacar?'))
        while l_ataque<0 or l_ataque>9:
            print('Linha inválida!')
            l_ataque = int(input('Qual linha deseja atacar?'))
    
        c_ataque = int(input('Qual coluna deseja atacar?'))
        while c_ataque>9 or c_ataque<0:
            print('Coluna inválida!')
            c_ataque = int(input('Qual coluna deseja atacar?'))

        coor_ataque = [l_ataque,c_ataque]
        if coor_ataque in ataques_jogador:
            print('A posição linha {} e coluna {} já foi informada anteriormente!' .format(l_ataque,c_ataque))
        else:
            ataques_jogador.append(coor_ataque)
            tabuleiro_oponente = faz_jogada(tabuleiro_oponente,l_ataque,c_ataque)
            jogada_jogador = False
            if afundados(frota_oponente,tabuleiro_oponente)==10:
                print('Parabéns! Você derrubou todos os navios do seu oponente!')
                jogando = False


            else:
                l_oponente = random.randint(0,9)
                c_oponente = random.randint(0,9)
                coor_oponente = [l_oponente,c_oponente]
                while coor_oponente in ataques_oponente:
                    l_oponente = random.randint(0,9)
                    c_oponente = random.randint(0,9)
                    coor_oponente = [l_oponente,c_oponente]
                
                ataques_oponente.append(coor_oponente)
                print('Seu oponente está atacando na linha {} e coluna {}' .format(l_oponente,c_oponente))
                tabuleiro_jogador = faz_jogada(tabuleiro_jogador,l_oponente,c_oponente)
                if afundados(frota,tabuleiro_jogador)==10:
                    print('Xi! O oponente derrubou toda a sua frota =(')
                    jogando = False
