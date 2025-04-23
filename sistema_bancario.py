menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
saldo = 0
saque = 0
limite = 500
extrato = " "
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    
    print('\nQual operação você deseja fazer? ')
    opcao = input(str(menu)).upper().strip()[0]
    
    if opcao == 'D':
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print(f"Operação falhou! O Valor R$ {valor:.2f} informado é invalido.")
    
    elif opcao == 'S':
        valor = float(input('Informe o valor do saque:'))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
    
        excedeu_saque = numero_saque >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            
        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")
    
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque += 1
            
        else:
            print("Operação falhou! O valor informado é inválido.")    

    elif opcao == "E":
        print("\n################# EXTRATO ###############")
        print("não foram realizado movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================================")
        
    elif opcao == "Q":
        break
    
    else: 
        print("Operação invalida, por favor selecione novamente a operação desejada!")
