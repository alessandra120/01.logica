import os
os.system ("clear")

valor_do_produto = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input("""
1 - A vista
2 - Parcelado                                                             
Digite a forma de pamento: """))

match forma_de_pagamento:
    case 1:
        # Aplicando desconto de 10%.
        desconto = valor_do_produto * 0.10
    case 2:
        a_vista = valor_do_produto
    case 3:
        1 - parcelado = valor_do_produto / 2
        2 - parcelado = valor_do_produto / 3
        3 - parcelado = valor_do_produto / 4
        4 - parcelado = valor_do_produto / 5
        5 - parcelado = valor_do_produto / 6
        6 - parcelado = valor_do_produto / 7
        7 - parcelado = valor_do_produto / 8
        8 - parcelado = valor_do_produto / 9
        9 - parcelado = valor_do_produto / 10
    case 4:
        1 - ("Vo")

    print("f\n")

