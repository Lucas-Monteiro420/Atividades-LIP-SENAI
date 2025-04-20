print ("\n====================== ATIVIDADE 1 ========================")

'''Desenvolva um programa que solicite ao usuário dois números
   e calcule a soma entre eles, exibindo o resultado na tela.'''

N1 = float(input("\nDigite o valor do primeiro número: "))
N2 = float(input("Digite o valor do segundo número: "))
Resultado = N1 + N2

print(f"\nO valor da soma dos dois números é {Resultado}")

print ("\n====================== ATIVIDADE 2 ========================")

'''Crie um programa que verifique a idade de uma pessoa
   e informe se ela tem permissão para acessar determinado conteúdo.
   A idade mínima permitida é 18 anos.'''

Idade = int(input("\nQual a sua idade? "))
Permissao = Idade

if Permissao >= 18:
    print("Idade permitida.")
else:
    print("Idade não permitida.")

print ("\n====================== ATIVIDADE 3 ========================")

'''Desenvolva um programa que calcule a área de um círculo.
   O programa deve solicitar ao usuário o valor do raio e calcular a área
   utilizando a fórmula A = π × r², onde π (pi) é aproximadamente 3,14.'''

Raio = float(input("\nDigite o valor do raio de círculo: "))

Area = 3.14 * Raio ** 2

print(f"\nA área do círculo é {Area:2.2f} (3.14 vezes o valor do Raio elevado ao quadrado).")

print ("\n====================== ATIVIDADE 4 ========================")

'''Elabore um programa que calcule a média de duas avaliações escolares.
   O programa deve solicitar as notas das duas provas, calcular a média aritmética e
   informar se o aluno foi aprovado ou reprovado. A média mínima para aprovação é 7,0.'''

Prova1 = float(input("\nDigite a nota obtida na primeira avaliação: "))
Prova2 = float(input("Digite a nota obtida na segunda avaliação: "))

Media = (Prova1 + Prova2) / 2

if Media >= 7:
    print(f"\nA média obtida nas duas avaliações foi de: {Media:2.2f}.")
    print("Parabéns! Você foi aprovado!")

else:
    print(f"\nA média obtida nas duas avaliações foi de: {Media:2.2f}.")
    print("Você foi reprovado!")

print ("\n====================== ATIVIDADE 5 ========================")

'''Crie um programa que calcule o consumo de combustível de um veículo.
   O programa deve solicitar a distância percorrida e calcular quantos litros foram gastos,
   considerando que o veículo consome 1 litro a cada 13 quilômetros.
   Em seguida, calcule o valor gasto em reais com base no preço do combustível informado pelo usuário.'''

D1 = float(input("\nDigite a distância percorrida: "))

Litros = 13
LitrosGastos = D1 / Litros

print(f"\nA quantidade de litros gastos até o destino final é de {LitrosGastos:2.2f} "
      f"(Considerando que o veículo consome 1 litro a cada 13 quilômetros).")

ValorLitroCombustivel = float(input("\nPara calcular o valor gasto em dinheiro"
                                    ", primeiro, digite o valor do combustível por litro: "))

ValorTotalGasto = LitrosGastos * ValorLitroCombustivel

print(f"O valor total gasto em combustível é de {ValorTotalGasto:2.2f} reais.")

print ("\n====================== ATIVIDADE 6 ========================")

'''Desenvolva um programa que simule o funcionamento de uma máquina.
   O programa deve perguntar ao usuário se deseja ligar a máquina.
   Se a resposta for "SIM", exiba a mensagem "MÁQUINA LIGADA" e faça a pergunta novamente.
   Se a resposta for "NÃO", exiba a mensagem "MÁQUINA DESLIGADA" e encerre o programa.
   Caso a resposta seja diferente, exiba uma mensagem de erro.'''

Opcoes = " "

while Opcoes.upper() != "NÃO":
    Opcoes = input("Deseja ligar a máquina? Digite SIM ou NÃO: ")
    if Opcoes.upper() == "SIM":
        print("MÁQUINA LIGADA")
    elif Opcoes.upper() != "NÃO":
        print("Opção inválida. Digite SIM ou NÃO.")

print("MÁQUINA DESLIGADA")

print ("\n====================== ATIVIDADE 7 ========================")

'''Elabore um programa que calcule a soma de todos os números ímpares menores que 100
   que são divisíveis por 3. O programa deve exibir cada número somado e o resultado final.'''

Soma= 0
Numero = 1

while Numero < 100:
    if Numero %  2 != 0 and Numero % 3 == 0:
        print(f"{Numero} +")
        Soma = Soma + Numero
    Numero = Numero + 2
print(f"\n= {Soma}")

print ("\n====================== ATIVIDADE 8 ========================")

'''Crie um programa que leia a altura de 6 pessoas e determine a maior e a menor altura entre elas.'''

Altura = float(input("\nDigite a altura da pessoa 1: "))

Medidor = 1
MaiorAltura = Altura
MenorAltura = Altura

while Medidor < 6:
    Medidor = Medidor + 1
    Altura = float(input(f"Digite a altura da pessoa {Medidor}: "))
    if Altura > MaiorAltura:
        MaiorAltura = Altura
    else:
        if Altura < MenorAltura:
            MenorAltura = Altura

print(f"\nA maior altura do grupo é {MaiorAltura}."
      f"\nA menor altura é {MenorAltura}.")

print ("\n====================== ATIVIDADE 9 ========================")

'''Desenvolva uma calculadora simples que realize as quatro operações básicas
   (adição, subtração, multiplicação e divisão). O programa deve solicitar dois números
   e a operação desejada, e então calcular o resultado utilizando funções específicas para cada operação.'''

#Subprograma 1
def somar (num1, num2):
    res= num1 + num2

    return res

#Subprograma 2
def subtrair (num1, num2):
    res = num1 - num2

    return res

#Subprograma 3
def multiplicar (num1, num2):
    res = num1 * num2

    return res

#Subprograma 4
def dividir (num1, num2):
    res = num1 / num2

    return res

#Programa principal

num1 = float(input("Digite o valor do primeiro número: "))
num2 = float(input("Digite o valor do segundo número: "))
Operacao = input("Digite a operação que deseja realizar, + ou - ou * ou /: ")

if Operacao == "+":
    res = somar(num1, num2)
elif Operacao == "-":
    res = subtrair(num1, num2)
elif Operacao == "*":
    res = multiplicar(num1, num2)
elif Operacao == "/":
    res = dividir(num1, num2)
else:
    print("Operação inválida!")
    res = None

print(f"Resultado: {res}")

print ("\n====================== ATIVIDADE 10 =======================")

'''Elabore um programa que leia 5 números e realize três operações: encontrar o maior número,
   o menor número e calcular a média entre eles. O programa deve utilizar funções separadas para cada uma
   dessas operações.'''

#Subprograma 1
def maior_numero (num1, num2, num3, num4, num5):
    Maior = num1
    if num2 > Maior:
        Maior = num2
    if num3 > Maior:
        Maior = num3
    if num4 > Maior:
        Maior = num4
    if num5 > Maior:
        Maior = num5

    return Maior

#Subprograma 2
def media (num1, num2, num3, num4, num5):
    Res = (num1 +  num2 + num3 + num4 + num5) /5

    return Res

#Subprograma 3
def menor_numero (num1, num2, num3, num4, num5):
    Menor = num1
    if num2 < Menor:
        Menor = num2
    if num3 < Menor:
        Menor = num3
    if num4 < Menor:
        Menor = num4
    if num5 < Menor:
        Menor = num5

    return Menor

#Programa Principal
num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))
num5 = float(input("Digite o quinto número: "))

Maior = maior_numero(num1, num2, num3, num4, num5)
Menor = menor_numero(num1, num2, num3, num4, num5)
Media = media(num1, num2, num3, num4, num5)

print(f"\nO maior número é: {Maior}")
print(f"O menor número é {Menor}")
print(f"A média dos números é {Media}")

print ("\n====================== ATIVIDADE 11 =======================")

'''Crie um programa que receba três valores (A, B e C) e aplique as seguintes regras:
   (1) Se A for maior que B, divida A por 2;
   (2)Se B for maior que C, some 2 ao valor de B;
   Ao final, exiba os valores finais de A, B e C.'''

A = float(input("\nEscreva o valor de A: "))
B = float(input("Escreva o valor de B: "))
C = float(input("Escreva o valor de C: "))

if A > B:
    A = A / 2
if B > C:
    B = B + 2

print("Valores Finais:"
      f"\nA = {A}"
      f"\nB = {B}"
      f"\nC = {C}")

print ("\n====================== ATIVIDADE 12 =======================")

'''Desenvolva um programa que receba um valor X e incremente esse valor em 1 repetidamente,
   exibindo cada novo valor, até que X seja maior ou igual a 10.
   Nesse momento, o programa deve encerrar.'''

X = float(input("Digite o valor de X: "))

while True:
    X = X + 1
    print(X)
    if X >= 10: break










