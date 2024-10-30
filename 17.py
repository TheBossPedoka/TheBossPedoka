import random
print('\033[1;34mEscolha um número entre 0 e 5. Tente advinhar...\033[m')
s=(0,1,2,3,4,5)
e=random.choice(s)
r=int(input('Em que número pensei? '))
if r == e:
    print('\033[1;35mParabéns! Você conseguiu me vencer!\033[m')
else:
    print(f'\033[1;31mVocê Perdeu! Eu pensei no numero {e} e não no {r}\033[m')
