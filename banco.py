#cadastro de usuario e senha
saldo = 0.0 #varialvel que guarda o saldo do usuario
#declara funçao
def validar_senha():
    senha_validar = input(" degite sua senha")
    if senha_validar== senha: 
     return True # retorna verdadeiro
    saldo =0.0
while True:
    print("bem vindoo!\n digite 1.deposito 2. sacar 3.pix 4.extrato 5.encerrar!")
    #ler a escolha do usuario 
    escolha_menu = int(input())#le a escolha como um numero
    #se usuario escolher cadastro
    if escolha_menu== 1:
        usuario= input("crie um nome de usuario ")
        senha = input("crie uma senha ")
    elif escolha_menu == 2: #se usuario escolher login
        #comparar as inf. cadastradas com uma leitura
        login_usuario = input ("degite seu usuario ")
        login_senha = input("degite sua senha ")
        if login_usuario == usuario and login_senha == senha:
            print("login realizado com secesso")
            #se login correto, entra no
            #menu principal do app
            print("bem vindo", usuario)
            while True: #enquanto que exiba o menu principal
                print("1.deposito 2. sacar 3.extrato 4.encerrar")
                escolha_principal = int(input())
                if escolha_principal == 1: # se o usuario escolher depositar 
                    #ler o valor do deposito
                    valor_deposito = float(input())
                    saldo = saldo + valor_deposito#atualiza o valor
                    print("novo saldo e ", saldo)
                elif escolha_principal ==2:#saque
                    valor_saque= float(input("degite o valor do saque "))
                    if validar_senha(): #se a senha correta
                        saldo = saldo - valor_saque
                    else:
                        print("senha incorreta")
                elif escolha_principal == 3:# se usuario escolher pix
                    valor_pix = float (input("degite o valor do pix"))
                    if validar_senha():
                        saldo = saldo - valor_pix
                    else:
                        print("senha incorreta")
                elif escolha_principal == 4: #se usuario escolher
                    
                    if validar_senha():
                        print("extrato:,saldo")
                    else:
                        print("senha incorreta")
                elif escolha_principal== 5: #encerrar
                    if validar_senha():
                        break               
                    else:
                          print("usuario ou senha incorreta")
        else:
            print("Senha errada")