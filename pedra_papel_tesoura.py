import random
import  emoji
print('-='*20)
print('\033[0:31mVamos Jogar\033[m\n\033[0:34mPedra\033[m,\033[0:33mPapel\033[m,\033[0:37mTesoura\033[m')
print('-='*20)
jogador = []
nome = ['Pedra', 'Papel', 'Tesoura']
sorteio = random.choice(nome)
#print(f'Eu escolho {sorteio}')
while jogador != sorteio:
    jogador = input('Digite >Pedra,Papel,Tesoura<: ').title()
    nome = ['Pedra', 'Papel', 'Tesoura']
    print(f'Eu escolho {sorteio}')
    if sorteio=='Pedra' and jogador =='Papel' or sorteio=='Papel' and jogador =='Tesoura' or sorteio=='Tesoura' and jogador =='Pedra':
        print(f'\033[34mParábens vocè ganhou!!!{emoji.emojize(":rosto_sorridente_com_3_corações:",language="pt")}\033[m')
    elif sorteio == 'Papel' and jogador =='Pedra' or sorteio=='Tesoura' and jogador =='Papel' or sorteio=='Pedra' and jogador =='Tesoura':
        print(f'\033[0:30m{emoji.emojize(":computador_de_mesa:",language="pt")}Eu ganhei!!!\033[m')
else:
    sorteio == 'Papel' and jogador == 'Papel' or sorteio == 'Tesoura' and jogador == 'Tesoura' or sorteio == 'Pedra' and jogador == 'Pedra'
    print(f'\033[0:33mEmpatamos!!!{emoji.emojize(":mãos_aplaudindo:",language="pt")}\033[m')
