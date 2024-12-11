#declarar uma função
def saudacoes(hora_do_dia): #exibir a saudação correspondente a hora do dia
    #dar bom dia
    if (hora_do_dia >= 0) and (hora_do_dia <= 12):
        print("bom dia!")
    #dar boa tarde
    elif (hora_do_dia >= 13) and (hora_do_dia <=18):
        print("boa tarde!")
    #dar boa noite
    elif (hora_do_dia >= 18) and (hora_do_dia <=23):
        print("boa noite!")
        
#peço para  usuario dizer a hora atual
resposta = int(input("digite que horas são:\n"))
#chama a função passando para ela o parametro obrigatorio
saudacoes(resposta)
