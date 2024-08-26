# O problems do Chocolate 
"""
 Um professor precisa sortear bombons para diversos alunos.Esses alunos serão sorteados randômicamente. O número deve corresponder ao número do diário 
"""

import random

#looping - interação - repetição - laço
while True:
    # padrão snake_cas ( PEP-8)
    sorteio_turma = random.randint(1,25)
    print(sorteio_turma)
    resposta = input("Deseja sortear outro número? (s/n)").strip().lower()
    if resposta != "s":
        print('encerrando o sorteio')
        break
