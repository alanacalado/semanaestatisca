import os
import time 

while True:

    os.system('cls') 
    nome = input("Informe o nome para calcular o imc ou deixe em branco para sair: ")

    if nome != "":
        altura = float(input("Digite a sua altura: ").replace(',','.').strip())
        os.system('cls')
        peso = float(input("Digite o seu peso: ").replace(',','.').strip())
        os.system('cls') 

        imc = peso / (altura * altura)
    
        if  imc  < 17:
            print(f"{nome} está com anorexia.")
        elif imc < 18.5:
            print(f"{nome} está abaixo do peso") 
        elif  imc  < 25:
            print(f"{nome} está no peso ideal.")
        elif imc < 30:
            print(f"{nome} está acima do peso.")
        elif imc  < 35:
            print(f"{nome} está com grau de obesidade I.")
        elif imc < 40.5:
            print(f"{nome} está com grau de obesidade II.")
        else:  
            print(f"{nome} está com grau de obesidade mórbida.")
    else:
        break