#cadastro de usuario e senha
saldo = 0.0 #variavel que guarda o saldo do usuario
while True:
    #menu principal
    print("bem vindo! \n digite 1.cadastro 2.login 3.encerrar")
    #ler a escolha do usario
    escolha_menu = int(input()) #le a escolha como um numero...

    #se usuario escolhar cadastro
    if escolha_menu == 1:
        #criar um usuario e uma senha com tipo sting
        usuario = input("crie um nome de usuario")
        senha = input("crie uma senha")
    elif escolha_menu == 2: #se o usuario escolher login
        #comparar as inf. cadastrada com uma leitura
        logim_usuario = input("digite usuario")
        logim_senha = input("digite a sua senha")
        if logim_usuario== usuario and logim_senha == senha:
            print("login realizado com sucesso")
            #se login corre, emtrar no
            #menu principal do app
            print("bem vindo", usuario)
            while True:# enquanto que exibira o menu principal
                print("1.deposito 2.sacar 3.pix 4.extrato 5.encerrar")
                escolha_principal = int(input())
                if escolha_principal == 1:#se usuario escolher depositar
                    #le o valor a ser depositado
                    valor_deposito = float(input())
                    saldo = saldo + valor_deposito #atualizar o valor
                    print("novo saldo é",saldo)
                elif escolha_principal ==2:#saque
                    valo_saque = float(input("digite o valor do saque"))
                    senha_saque = input("digite sua senha")
                    if senha_saque ==senha: #se senha incorreta
                        saldo = saldo - valo_saque #subtrai o valor do saldo
                    else:  
                        print("senha incorreta")
                elif escolha_principal == 3: #se usuario escolhar pix
                    valor_pix = float(input("digite o valor do pix"))
                    senha_pix = input("digite sua senha")
                    if senha_pix == senha:
                        saldo = saldo - valor_pix
                    else:
                        print("senha incorreta")
                elif escolha_principal == 4: #se usuario escolher visualizar
                    senha_extrato = input("digite sua semha")
                    if senha_extrato == senha:
                       print("extrato:", saldo)
                    else:
                        print("senha incorreta")
                elif escolha_principal == 5: #encerrar
                    senha_encerrar = input("digite sua senha")
                    if senha_encerrar == senha:
                        break
                    else:
                        print("senha incorreta")

            