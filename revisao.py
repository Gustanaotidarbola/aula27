#ler entradas do usuarios
cont = 0#variavel que controla a repetição
escolha_usuario = int(input("quantidade de aluno ")) #variavel que guarda quantas vezes o codigo vai rodar
alunos = []
while cont <= escolha_usuario:
    nome = input("nome do aluno ")#armazenar o nome do aluno
    nota1 = float(input("nota do 1 bimestre "))#ler 4 notas do aluno
    nota2 = float(input("nota do 2 bimestre "))
    nota3 = float(input("nota do 3 bimestre "))
    nota4 = float(input("nota do 4 bimestre "))

    faltas = int(input("faltas "))#calculo da media
    media = (nota1+nota2+nota3+nota4)/4

    #logica da situação
    if faltas >31:
        situacao = "reprovado por falta"
    elif media >=8:
        situacao = "aprovado"
    elif media >=5:#recuperação
        recuperacao = float(input("nota da recuperação "))#ler a nota da recuperação
        if recuperacao >= (10-media):
            situacao = "aprovado na recuperação"
        else:
            situacao = "reprovado na recuperação"
    else:
        situacao = "reprovado por media"
    alunos.append([nome,faltas,media,situacao])
    #relatorio
print(alunos)
    
