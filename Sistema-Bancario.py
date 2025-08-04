menu = f"""
    ######### CONTA BANCÁRIA #########
    [1] - Deposito
    [2] - Saque
    [3] - Extrato
    [0] - Sair
    ##################################
"""

saldo_conta = 0
extrato_conta = ""
quantidade_saques = 3
VALOR_MAXIMO_SAQUES = 500

while True: 
    
    opcao = int(input(menu))
    
    if opcao == 1:
        valor_depositado = float(input("Informe o valor que será depositado: "))
        
        if(valor_depositado < 0):
            print("Não é possível depositar valores negativos, tente novamente!")
        else:
            saldo_conta += valor_depositado
            extrato_conta += f"\n Deposito no valor de R${valor_depositado:.2f}"
            print(f"R${valor_depositado}")
        
        
    elif opcao == 2:
        
        valor_saque = float(input("Informe o valor que deseja sacar: "))
        
        if valor_saque > saldo_conta:
            print("Saldo insuficiente, tente novamente com um valor menor!")
        elif valor_saque > VALOR_MAXIMO_SAQUES:
            print(f"Valor de saque maior que o limite total por saque, tente novamente com um valor abaixo de: R${VALOR_MAXIMO_SAQUES:.2f}")
        elif quantidade_saques == 0:
            print("Quantidades de saques diários foi excedido, tente novamente outro dia!")
            
        elif valor_saque > 0:
            saldo_conta -= valor_saque
            extrato_conta += f"\n Saque realizado no valor R${valor_saque:.2f}"
            quantidade_saques -= 1;
        
        
        
    elif opcao == 3:
        #print(extrato_conta)
        print("\n#################EXTRATO#################")
        print("Não foram realizadas movimentações" if not extrato_conta else extrato_conta)
        print(f"\n Saldo da Conta: R$ {saldo_conta:.2f}")
        print("#########################################")
    elif opcao == 0:
        break
    else:
        print("Operação Inválida, tente novamente!")
        