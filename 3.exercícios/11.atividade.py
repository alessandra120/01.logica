import os
os.system ("clear")

# DESENVOLVA UM PROGRAMA QUE RECEBA COMO ENTRADA UM NÚMERO INTEIRO QUE
# REPRESENTE UM DOS 7 DIAS DA SEMANA E IMPRIMA NA TELA SE ESSE DIA É ÚTIL
# FINAL DE SEMANA OU INVÁLIDO, 
# CONSIDERE QUE DOMINGO É DIA 1 E SÁBADO O DIA 7.

# ENTRADA
Dia = int(input("Digite um número para o dia da semana: "))

# PROCESSAMENTO
match Dia:
    case 1:
        print("domingo - 1")
    case 2:
        print("segunda-feira - 2")
    case 3:
        print("terça-feira - 3")
    case 4:
        print("quarta-feira - 4")
    case 5:
        print("quinta-feira - 5")
    case 6:
        print("sexta-feira - 6")
    case 7:
        print("sábado - 7")

        



