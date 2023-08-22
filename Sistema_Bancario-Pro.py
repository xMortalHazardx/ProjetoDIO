

saldo = 0.00

contador = []

for i in range(3):    

    contador = i, saldo

    print(""" ==================|Bem vindo ao Banco Milion|==========
                 
          {Atenção: Você possui 3 transações para realizar diariamente,
          caso exceda o limite, deverá retornar no proximo dia útil.}

                | Para saldo: Digite a tecla | (1)
                | Para saque: Digite a tecla | (2)
                | Para extrato: Digite a tecla | (3)
                | Para depósito: Digite a tecla | (4)
                | Digite para Sair. | (0)
                    
            OBS: Somente faça um saque se houver saldo.
============================================================""")

    
    opcao = int(input("Digite uma das opções acima: "))

    if opcao == 1:
    
        print("Seu saldo é: ", (saldo))


    elif opcao == 2:

        saque = float(input("Digite o valor que deseja sacar: "))
        saldo = saldo - saque

        if saldo < saque:
            print("Saldo insuficiente, gentileza realize um deposito para concluir a transação!!")

        elif saque > 500.00:
     
            print("Limite de saque deverá ser de até 500 reais")

    elif opcao == 3:
        print("Este é o seu extrato do banco: ", contador)

    elif opcao == 4:

        deposito = float(input("Digite o valor que deseja depositar: "))
        if deposito > 500.00:
            
            print("Limite de depósito deverá ser até 500 reais")
        else:
            saldo = saldo + deposito
    
    elif opcao == 0:

        print(""" ==================|Banco Milion|==================
       
              Agradecemos a confiança em escolher o nosso banco!!!

==================|Até a próxima.|==================""")
        break
    else:
        print("Opção invalida tente novamente!")
        i -= 1
  



