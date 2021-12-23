dici = {('id_jogador 1', 'eu'):'qualquer coisa aí'}
for i in range(4):
    print('entrou!', dici)
    if i == 1:
        del dici[('id_jogador 1', 'eu')]