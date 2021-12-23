from base_do_jogo import game, boas_vindas, palavras, palavra_aleatoria_dici

def multiplayers():
    
    ps = palavras()
        
    multiplayers = int(input('Entre com o número de jogadores: [2] jogadores, [3] jogadores ou [4] jogadores\n>>> '))
    nomes_jogadores = []
    dici_vez_jogador = {}
    
    while multiplayers not in range(1,5):
        print('Deu zebra!')
    
    cont = 0
    for jogador in range(multiplayers):
        nome_jog = input(f'\n Digite o nome do jogador {jogador +1}: ')
        nomes_jogadores.append(nome_jog)
        
        cont += 1
        dici_vez_jogador[(f'id_jogador {cont}', nome_jog)] = palavra_aleatoria_dici(ps)
    
    boas_vindas(multiplayers, nomes_jogadores)    
    
    if multiplayers == 2:
        nome1 = nomes_jogadores[0]
        nome2 = nomes_jogadores[1]
        
        lista1 = ['_'] * len(dici_vez_jogador[('id_jogador 1', nome1)])
        lista2 = ['_'] * len(dici_vez_jogador[('id_jogador 2', nome2)])
        
        
        chances1 = 6
        chances2 = 6
        tem_alguem_jogando = True
        while tem_alguem_jogando:
            
            nome1 = nomes_jogadores[0]
            if ('id_jogador 1', nome1) in dici_vez_jogador:     # JOGADOR 1
                
                print(f'Essa é a partida do jogador 1: {nome1}')
                
                erro = False    
                while not erro:
                
                    
                    (enforcou, acertou, chances1, erro) = game(dici_vez_jogador[('id_jogador 1', nome1)], lista1, chances1)
                    
                if enforcou == True:
                    print('E enforcou! Tente na próxima.\n\n')
                    del dici_vez_jogador[('id_jogador 1', nome1)]
                    
                    
                elif acertou == True:
                    print('Parabéns, você acertou todas as letras!!', dici_vez_jogador[('id_jogador 1', nome1)].upper(),'\n\n')
                    del dici_vez_jogador[('id_jogador 1', nome1)]
                    
                    
            nome2 = nomes_jogadores[1]
            if ('id_jogador 2', nome2) in dici_vez_jogador:
                print(f'Essa é a partida do jogador 2: {nome2}') # JOGO
                erro = False    
                while not erro:
                        
                    (enforcou, acertou, chances2, erro) = game(dici_vez_jogador[('id_jogador 2', nome2)], lista2, chances2)
            
                if enforcou == True:
                    print('E enforcou! Tente na próxima.\n\n')
                    del dici_vez_jogador[('id_jogador 2', nome2)]
                    
                elif acertou == True:
                    print('Parabéns, você acertou todas as letras!!', dici_vez_jogador[('id_jogador 2', nome2)].upper(),'\n\n')
                    del dici_vez_jogador[('id_jogador 2', nome2)]
            
            if ('id_jogador 1', nome1) not in dici_vez_jogador and ('id_jogador 2', nome2) not in dici_vez_jogador:
                print('=-=-FIM DE JOGO!!-=-=\n\n')
                tem_alguem_jogando = False                
        
    elif multiplayers == 3:
        print('Estamos em construção, tente outro número (tipo, 2).')
        # tem_alguem_jogando = True
        # while tem_alguem_jogando:
            
        #     nome1 = nomes_jogadores[0]
        #     if ('id_jogador 1', nome1) in dici_vez_jogador:
        #         print('Essa é a partida do jogador 1: Está jogando enquanto estiver o nome no dicionario') # JOGO
        #         erro = False    
        #         while not erro:
                
        #             jogador1 = game()
        
        #     nome2 = nomes_jogadores[1]
        #     if ('id_jogador 2', nome2) in dici_vez_jogador:
        #         print('Essa é a partida do jogador 1: Está jogando enquanto estiver o nome no dicionario') # JOGO
        #         erro = False    
        #         while not erro:
                    
        #             jogador2 = game()
            
        #     nome3 = nomes_jogadores[2]
        #     if ('id_jogador 3', nome3) in dici_vez_jogador:
        #         print('Essa é a partida do jogador 1: Está jogando enquanto estiver o nome no dicionario') # JOGO
        #         erro = False    
        #         while not erro:
            
        #             jogador3 = game()
        
    else:
        print('Estamos em construção tente outro número (tipo, 2).')
    #     # print('Jogo de 4 players!')
    #     # print(f'Bem vindo ao jogo, {nomes_jogadores[0]}, {nomes_jogadores[1]}, {nomes_jogadores[2]} e {nomes_jogadores[3]}')
        
    #     jogador1 = game()
    #     jogador2 = game()
    #     jogador3 = game()
    #     jogador4 = game()

multiplayers()      # Chamando a função
