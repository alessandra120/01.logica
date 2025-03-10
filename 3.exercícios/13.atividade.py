import os
os.system ("clear")
#Solicite que o usuário informe o valor de um produto e a forma de pagamento.
#1 - Pagamento à vista;
#2 - Pagamento à prazo.
#Se o produto for pago à vista aplique um desconto de 10% antes de mostrar o valor final, senão informe o mesmo
#valor do produto.
#Se for escolhida a opção de pagamento à prazo, solicite que o usuário digite a quantidade de parcelas que ele
#deseja pagar. Podendo parcelar em até 6 vezes.
#No final, mostre:
#Se o pagamento for à vista: 
#	Valor do produto: R$ 100,00
#Forma de pagamento: à vista
#Valor do desconto: R$ 10,00
#Total a pagar: R$ 90,00
#Se o pagamento for à prazo:
#Valor do produto: R$ 100,00
#Forma de pagamento: à prazo
#Quantidade de parcelas: 6
#Valor por parcela: R$ 16,66
#Total à prazo: R$ 100,00


valor_do_produto = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input("""
1 - A vista
2 - Parcelado                                                             
Digite a forma de pagamento: """))

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
    case 4:
        1 - ("Vo")

    print(f"\n")

