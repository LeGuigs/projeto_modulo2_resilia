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


         nome1 = nomes_jogadores[0]
         nome2 = nomes_jogadores[1]
         nome3 = nomes_jogadores[2]

         lista1 = ['_'] * len(dici_vez_jogador[('id_jogador 1', nome1)])
         lista2 = ['_'] * len(dici_vez_jogador[('id_jogador 2', nome2)])
         lista3 = ['_'] * len(dici_vez_jogador[('id_jogador 3', nome3)])

         chances1 = 6
         chances2 = 6
         chances3 = 6

         tem_alguem_jogando = True
         while tem_alguem_jogando:

             nome1 = nomes_jogadores[0]
             if ('id_jogador 1', nome1) in dici_vez_jogador:
                 print('Essa é a partida do jogador 1: Está jogando enquanto estiver o nome no dicionario')  # JOGO
                 erro = False
                 while not erro:
                     (enforcou, acertou, chances1, erro) = game(dici_vez_jogador[('id_jogador 1', nome1)], lista1,
                                                                chances1)

                 if enforcou == True:
                     print('E enforcou! Tente na próxima.\n\n')
                     del dici_vez_jogador[('id_jogador 1', nome1)]

                 elif acertou == True:
                     print('Parabéns, você acertou todas as palavras!!',
                           dici_vez_jogador[('id_jogador 1', nome1)].capitalize(), '\n\n')
                     del dici_vez_jogador[('id_jogador 1', nome1)]

             nome2 = nomes_jogadores[1]
             if ('id_jogador 2', nome2) in dici_vez_jogador:
                 print('Essa é a partida do jogador 2: Está jogando enquanto estiver o nome no dicionario')  # JOGO
                 erro = False
                 while not erro:
                     (enforcou, acertou, chances2, erro) = game(dici_vez_jogador[('id_jogador 2', nome2)], lista2,
                                                                chances2)

                 if enforcou == True:
                     print('E enforcou! Tente na próxima.\n\n')
                     del dici_vez_jogador[('id_jogador 2', nome2)]

                 elif acertou == True:
                     print('Parabéns, você acertou todas as palavras!!',
                           dici_vez_jogador[('id_jogador 2', nome2)].capitalize(), '\n\n')
                     del dici_vez_jogador[('id_jogador 2', nome2)]

             nome3 = nomes_jogadores[2]
             if ('id_jogador 3', nome3) in dici_vez_jogador:
                 print('Essa é a partida do jogador 3: Está jogando enquanto estiver o nome no dicionario')  # JOGO
                 erro = False
                 while not erro:
                     (enforcou, acertou, chances3, erro) = game(dici_vez_jogador[('id_jogador 3', nome3)], lista3,
                                                                chances3)

                 if enforcou == True:
                     print('E enforcou! Tente na próxima.\n\n')
                     del dici_vez_jogador[('id_jogador 3', nome3)]

                 elif acertou == True:
                     print('Parabéns, você acertou todas as palavras!!',
                           dici_vez_jogador[('id_jogador 3', nome3)].capitalize(), '\n\n')
                     del dici_vez_jogador[('id_jogador 3', nome3)]

             if ('id_jogador 1', nome1) not in dici_vez_jogador and (
             'id_jogador 2', nome2) not in dici_vez_jogador and ('id_jogador 3', nome3) not in dici_vez_jogador:
                 print('fim de jogo')
                 tem_alguem_jogando = False

    else:
        print('Estamos em construção tente outro número (tipo, 2).')
        print('Jogo')

        nome1 = nomes_jogadores[0]
        nome2 = nomes_jogadores[1]
        nome3 = nomes_jogadores[2]
        nome4 = nomes_jogadores[3]

        lista1 = ['_'] * len(dici_vez_jogador[('id_jogador 1', nome1)])
        lista2 = ['_'] * len(dici_vez_jogador[('id_jogador 2', nome2)])
        lista3 = ['_'] * len(dici_vez_jogador[('id_jogador 3', nome3)])
        lista4 = ['_'] * len(dici_vez_jogador[('id_jogador 4', nome4)])

        chances1 = 6
        chances2 = 6
        chances3 = 6
        chances4 = 6

        tem_alguem_jogando = True
        while tem_alguem_jogando:

            nome1 = nomes_jogadores[0]
            if ('id_jogador 1', nome1) in dici_vez_jogador:
                print('Essa é a partida do jogador 1: Está jogando enquanto estiver o nome no dicionario')
                erro = false
                while not erro:
                    (enforcou, acertou, chances1, erro) = game(dici_vez_jogador[('id_jogador 1', nome1)], lista1,
                                                               chances1)

                if enforcou == True
                    print('E enforcou! Tente na próxima.\n\n')
                    del dici_vez_jogador[('id_jogador 1', nome1)]

                elif acertou == True
                    print('Parabéns, você acertou todas as palavras!!',
                          dici_vez_jogador[('id_jogador 1', nome1)].capitalize(), '\n\n')
                    del dici_vez_jogador[('id_jogador 1', nome1)]

        jogador1 = game()
        jogador2 = game()
        jogador3 = game()
        jogador4 = game()

    multiplayers()  # Chamando a função
