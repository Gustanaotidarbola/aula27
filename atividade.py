print("degite n1:")
n1= float(input())
print("degite n2:")
n2=float(input())
print("degite n3:")
n3= float(input())
print("degite n4:")
n4= float(input())
print("degite a quantidade de faltas do aluno:")
qntd_faltas= int(input())
media=((n1+n2+n3+n4)/4)

print("a media é :,media")
if media >=8:
    print("voce foi aprovado")
elif media >=5:
    print("voce esta na recuperacao")
elif media<5:
    print("voce foi reprovado") 
if qntd_faltas>=30:
    print("o aluno foi reprovado por quantidades de faltas")
           
