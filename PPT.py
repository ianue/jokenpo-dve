import random

pedra = str.upper('Pedra')
papel = str.upper('Papel')
tesoura = str.upper('Tesoura')
print ('Escolha : {} | {} | {} '.format(pedra, papel, tesoura))
escolha = str.upper(input('Qual é a sua opção? '))
ep = ["Pedra", "Papel", "Tesoura"]
me = str.upper(random.choice(ep))
print('=========================================')
print('Você escolheu : {} '.format(escolha))
print('Cierri Seti Careca escolheu : {} '.format(me))
print('|/|/|/|/|/|/|/|/|/|/|/|/|/|/|/|/|/|/|/|/|')