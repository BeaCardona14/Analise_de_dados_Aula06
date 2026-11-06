#Teste 5 entradas novas, prova01, prova02, prova03 utilze o while:
#Faça a média entre as provas e mostre a situação onde:
# Média >=7 aprovado; media >=5 recuperação; media <5 reprovado

aluno = 1
while aluno <=10:
    print(f"---- Aluno {aluno}----")
    nome = input("digite o nome do aluno: ")

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digte a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

   #Calcular média
    media =  (n1 + n2 + n3) / 3
    print(f"media: {media}")


#Verificar situação
    if media >= 7:
       situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "reprovado" 
    print(f"Situação: {situacao}")
    
    aluno += 1    


               