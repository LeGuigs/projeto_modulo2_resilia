from time import sleep
import random

def palavras():
    palavras_secretas = {'keys': ['_','_','_','_'],'reversed': ['_','_','_','_','_','_','_','_'],'input': ['_','_','_','_','_'],
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
            # print(letra)
            if chute == letra:      # Se chute/letra do usuário é igual a variável letra, então vai ser adicionado a letra na lista que está dentro do dicionário
                tracos_forca[ind] = letra        # na posição de acordo com o valor do índice (ind)
                sleep(0.1)
                mensagem_mais_tracinhos_da_forca('\nAcertou!! ', palavra_secr, tracos_forca)      # trancinhos vão aparecer de acordo com a quantidade de letras da palavra
                print('\n \n \n')
            ind += 1
        errou = False
            
        if falta_na_forca == 1:
            errou = True
                         
    elif chute in caracteres_especiais:
        print(f'Caracter especial usado ({chute}). Tente novamente!')           
                    
    else:                       # Senão, chances -1 até chegar 0
        errou = True
        numero_de_chances -= 1
        sleep(0.1)
        mensagem_mais_tracinhos_da_forca('\nErrou!! ', palavra_secr, tracos_forca)
        print('\n \n \n')
        desenha_forca(numero_de_chances)
        desenha_forca_final(numero_de_chances)
        print('\n \n \n')
                
    enforcou = numero_de_chances == 0         # variável enforcou recebe True se variável chances vale 0  
    acertou = falta_na_forca == 1      # variável acertou recebe True se variável/lista forca não conter underscore (-)
    return (enforcou, acertou, numero_de_chances, errou)

def boas_vindas(quantidade_de_jogadores, nomes_dos_jogadores):
    
    print(f'\nSEJA BEM-VINDO(A) AO JOGO DA FORCA')
    
    for posicao in range(len(nomes_dos_jogadores)):
        print(f'\tJogador {posicao+1}: ',nomes_dos_jogadores[posicao])
        
    print(f'\nJOGO COM {quantidade_de_jogadores} PLAYERS\nA palavra secreta é uma das palavras reservadas ou funções built-in do Python. Boa sorte!')
    pausa = input('Aperte ENTER para prosseguir.\n')
