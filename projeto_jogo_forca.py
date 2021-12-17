import random
from time import sleep

def palavras():
    palavras_secretas = {'keys': ['_','_','_','_'],'Reversed': ['_','_','_','_','_','_','_','_'],'input': ['_','_','_','_','_'],
                        'print': ['_','_','_','_','_'],'return': ['_','_','_','_','_','_'],'lower': ['_','_','_','_','_'],
                        'popitem': ['_','_','_','_','_','_','_'],'bleak': ['_','_','_','_','_'],'remove': ['_','_','_','_','_','_'],
                        'update': ['_','_','_','_','_','_'],'upper': ['_','_','_','_','_'],'append': ['_','_','_','_','_','_'],
                        'tuple': ['_','_','_','_','_'],'global': ['_','_','_','_','_','_'],'while': ['_','_','_','_','_'],
                        'enumerate': ['_','_','_','_','_','_','_','_','_'],'clear': ['_','_','_','_','_'],'items': ['_','_','_','_','_'],
                        'float': ['_','_','_','_','_'],'import': ['_','_','_','_','_','_'],}
    return palavras_secretas

def palavra_aleatoria_dici(dicionario_com_palavras_secretas):       # Escolhendo uma palavra aleatória após transformar as chaves dict() em list()
    uma_palavra_aleatoria = random.choice(list(dicionario_com_palavras_secretas.keys()))
    return uma_palavra_aleatoria

def desenha_forca(chances):
    print("  _______     ")
    sleep(0.1)
    print(" |/      |    ")
    sleep(0.1)

    if chances == 6:
        print(" |            ")
        sleep(0.1)
        print(" |            ")
        print(" |            ")
        sleep(0.1)
        print(" |            ")

    if chances == 5:
        print(" |      (_)   ")
        sleep(0.1)
        print(" |            ")
        sleep(0.1)
        print(" |            ")
        sleep(0.1)
        print(" |            ")

    if chances == 4:
        print(" |      (_)   ")
        sleep(0.1)
        print(" |       |    ")
        sleep(0.1)
        print(" |       |    ")
        sleep(0.1)
        print(" |            ")

    if chances == 3:
        print(" |      (_)   ")
        sleep(0.1)
        print(" |      \|    ")
        sleep(0.1)
        print(" |       |    ")
        sleep(0.1)
        print(" |            ")

    if chances == 2:
        print(" |      (_)   ")
        sleep(0.1)
        print(" |      \|/   ")
        sleep(0.1)
        print(" |       |    ")
        sleep(0.1)
        print(" |            ")

    if chances == 1:
        print(" |      (_)   ")
        sleep(0.1)
        print(" |      \|/   ")
        sleep(0.1)
        print(" |       |    ")
        sleep(0.1)
        print(" |      /     ")
    
def desenha_forca_final(chances):
        
    if chances == 0:
        print("  _______     ")
        sleep(0.1)
        print(" |/      |    ")
        sleep(0.1)
        print(" |      (_)   ")
        sleep(0.1)
        print(" |      \|/   ")
        sleep(0.1)
        print(" |       |    ")
        sleep(0.1)
        print(" |      / \   ")    

def mensagem_mais_tracinhos_da_forca(msg, palavra_secreta, forca):     # De acordo com a quantidade de letras da palavra
    if len(palavra_secreta) == 4:
        print(msg, forca[0], forca[1], forca[2], forca[3])
    elif len(palavra_secreta) == 5:
        print(msg, forca[0], forca[1], forca[2], forca[3], forca[4])
    elif len(palavra_secreta) == 6:
        print(msg, forca[0], forca[1], forca[2], forca[3], forca[4], forca[5])
    elif len(palavra_secreta) == 7:
        print(msg, forca[0], forca[1], forca[2], forca[3], forca[4], forca[5], forca[6])
    elif len(palavra_secreta) == 8:
        print(forca[0], forca[1], forca[2], forca[3], forca[4], forca[5], forca[6], forca[7])
    else:
        print(msg, forca[0], forca[1], forca[2], forca[3], forca[4], forca[5], forca[6], forca[7], forca[8])

def game(palavra_secr,tracos_forca, numero_de_chances):
    
    caracteres_especiais = '!@#$%¨&(){[}]~^//<?>ºª'    
    falta_na_forca = tracos_forca.count('_')       # Indicador de forca incompleta ou não
    print(f'\nVocê tem {numero_de_chances} chances e {falta_na_forca} letras para acertar')
    
    desenha_forca(numero_de_chances)
    
    chute = input('Digite uma letra que contém na palavra:\n>>> ')
    chute = chute.lower().strip()
    
    if chute in palavra_secr:        # Se chute/letra do usuário está na palavra 'upper' ele entra na condicional
        ind = 0
        for letra in palavra_secr:         # Percorrendo cada letra da CHAVE/ variável palavra
            
            if chute == letra:      # Se chute/letra do usuário é igual a variável letra, então vai ser adicionado a letra na lista que está dentro do dicionário
                tracos_forca[ind] = letra        # na posição de acordo com o valor do índice (ind)
                mensagem_mais_tracinhos_da_forca('\nAcertou!! ', palavra_secr, tracos_forca)      # trancinhos vão aparecer de acordo com a quantidade de letras da palavra
                print('\n \n \n')
                
            ind += 1
    
    elif chute in caracteres_especiais:
        print(f'Caracter especial usado ({chute}). Tente novamente!')           
    
    else:                       # Senão, chances -1 até chegar 0
        numero_de_chances -= 1
        mensagem_mais_tracinhos_da_forca('\nErrou!! ', palavra_secr, tracos_forca)      # trancinhos vão aparecer de acordo com a quantidade de letras da palavra
        
        desenha_forca_final(numero_de_chances)
        print('\n \n \n')
        
    enforcou = numero_de_chances == 0         # variável enforcou recebe True se variável chances vale 0  
    acertou = '_' not in tracos_forca      # variável acertou recebe True se variável/lista forca não conter underscore (-)
    return (enforcou, acertou, numero_de_chances)
    
def qtd_nome_dos_players():
    multiplayers = input('Entre com o número de jogadores: [2] jogadores, [3] jogadores ou [4] jogadores\n>>> ')
    names_players = []
    list_multiplayer = ['2', '3', '4']
    
    while multiplayers not in list_multiplayer:       # Repetir enquanto o usuário não escolher o número de players entre as opçãos mostrada 
        print('Deu zebra. É possível jogar apenas com 2 a 4 jogadores.')
        multiplayers = input('Entre com o número de jogadores: [2] jogadores, [3] jogadores ou [4] jogadores\n>>> ')
        
    for player in range( int(multiplayers) ):     # De acordo com a quantidade de players/jogadores perguntará os nomes
        name_pl = input(f'\n\tDigite o nome do jogador { player +1 }: ')
        names_players.append(name_pl)
    
    return (multiplayers, names_players)        # Retornando a quantidade de jogadores e a lista de nomes dos jogadores

def boas_vindas(quantidade_de_jogadores, nomes_dos_jogadores):
    
    print(f'\nSEJA BEM-VINDO(A) AO JOGO DA FORCA!')
    
    for posicao in range(len(nomes_dos_jogadores)):
        print(f'\tJogador {posicao+1}: ',nomes_dos_jogadores[posicao])
        
    print(f'\nJOGO COM {quantidade_de_jogadores} PLAYERS\nA palavra secreta é uma das palavras reservadas ou funções Built-in do Python. Boa sorte!')
    pausa = input('Aperte ENTER para prosseguir.\n')
    
'''Os parâmetros da multiplayer() meio que não serve para nada NO MOMENTO, mas servirão...'''
def multiplayer(quantidade_de_jogadores, nomes_dos_jogadores):
    
    boas_vindas(quantidade_de_jogadores, nomes_dos_jogadores)

    ps = palavras()     # Chamando o dicionario com as palavras secretas e traços da forca 
    
    jogar = True
    while jogar:    # Enquanto usuário escolher 'sim' (=True) o jogo se repetirá

        plvr_aleatoria = palavra_aleatoria_dici(ps)             
            
        for palavra, forca in ps.items():   # PALAVRA e FORCA percorre o dicionário palavras_secretas, respectivamente,
            if palavra == plvr_aleatoria:
                
                enforcou, acertou, chances = False, False, 6
                while enforcou == False and acertou == False:    # Enquanto chances vale + que 0 e a forca ainda está incompleta vai loopar.
                                                                # procurando por: CHAVES (palavra) e VALOR (underscore/letras acertadas)    
                    
                    (enforcou, acertou, chances) = game(palavra, forca, chances)    # Aqui rola a mágica / JOGO da Forca
                
                # Se uma das variáveis for TRUE entra na condicional.
                if enforcou:
                    print('E enforcou! Tente na próxima.\n\n')
                elif acertou:
                    print('Parabéns, você acertou todas as letras!!', palavra.capitalize(), '\n\n')
                
                jogar = input('Quer jogar ainda? [SIM] ou [NÃO] \n>>> ')
                jogar = jogar.lower().strip()
                
                while jogar != 'sim' and jogar != 'não':
                    jogar = input('Não entendi a sua resposta. Quer jogar ainda? [SIM] ou [NÃO] \n>>> ')
                    jogar = jogar.lower().strip()
                
                if jogar == 'sim':
                    jogar = True
                else:
                    jogar = False    

# Chamando a função com os nomes e as quantidades de jogadores       
(qtd_jogadores, nomes_jogadores) = qtd_nome_dos_players()

'''Destrinchar dentro do bloco multiplayer() variáveis/loop que varia de acordo com a quantidade de jogadores,
da forma que se encontra roda apenas um jogador independente da quantidade de jogadores.'''
# Chamando a função multiplayer que contém os jogadores e UMA partida de jogo para UM jogador/player
if qtd_jogadores == 2:
    multiplayers2 = multiplayer(qtd_jogadores, nomes_jogadores)
elif qtd_jogadores == 3:
    multiplayers3 = multiplayer(qtd_jogadores, nomes_jogadores)
else:
    multiplayers4 = multiplayer(qtd_jogadores, nomes_jogadores)
    
    
# Atualizações:
# 14/12/21 > Implementa nova oportunidade para caracteres especiais