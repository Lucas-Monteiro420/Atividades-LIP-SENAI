print ("\n====================== ATIVIDADE 1 ========================")

'''Soma dos Quadrados: Crie um programa que solicite ao usuário três valores inteiros
   A, B e C, calcule o quadrado de cada valor e apresente a soma desses quadrados.'''

print("\nPara calcular o quadrado de A, B e C, siga os passos abaixo:")

A = int(input("Digite o valor de A:"))
B = int(input("Digite o valor de B:"))
C = int(input("Digite o valor de C:"))

res = A**2 + B**2 + C**2
print("O resultado da soma do quadrado de A, B e C é de: ", res)

print ("\n====================== ATIVIDADE 2 ========================")

'''Desenvolva um programa que calcule quantos dias de vida um fumante perderá. 
   O programa deve solicitar a quantidade de cigarros fumados por dia e por quantos anos a pessoa é fumante. 
   Considere que cada cigarro reduz o tempo de vida em 10 minutos.'''

CigarrosFumados = float(input("Digite quantos cigarros você fuma diariamente: "))
TempoFumante = float(input("Há quanto tempo você fuma?"))
TempoPerdido =  CigarrosFumados * TempoFumante * 10 * 365
DiasPerdidosDeVida = TempoPerdido / 1440  #24 horas multiplicado por 60 minutos

print(f"\nVocê perderá aproximadamente {DiasPerdidosDeVida:1.0f} dias de vida devido ao tabagismo.")

print ("\n====================== ATIVIDADE 3 ========================")

'''Crie um programa que converta um período de tempo fornecido em 
   dias, horas, minutos e segundos para o total equivalente em segundos e milisegundos.'''

Dias = float(input("\nDigite a quantidades de dias: "))
Horas = float(input("Digite a quantidade de horas: "))
Minutos = float(input("Digite a quantidade de minutos: "))
Segundos = float(input("Digite a quantidade de segundos: "))

TotalSegundos = (Dias * 24 * 60 * 60) + (Horas * 60 *60) + (Minutos * 60) + Segundos
TotalMiliSegundos = TotalSegundos * 1000

print(f"\nO tempo convertido em segundos é de {TotalSegundos:2.2f} e em milisegundos é de {TotalMiliSegundos:2.2f}")

print ("\n====================== ATIVIDADE 4 ========================")

'''Desenvolva um programa que calcule o novo salário de um funcionário após um aumento percentual. 
   O usuário deve informar o salário atual e a porcentagem de aumento.'''

SalarioAtual = float(input("\nDigite o valor do salário atual do seu funcionário: R$"))
PorcentagemAumento = float(input("Digite o percentual a ser acrescentado: "))
AumentoTotal = SalarioAtual * (PorcentagemAumento / 100)
NovoSalario = SalarioAtual + AumentoTotal

print(f"\nO salário teve um aumento de {PorcentagemAumento}%, ou seja, {AumentoTotal} reais."
      f"\nO funcionário receberá, no próximo mês, {NovoSalario:2.2f} reais.")

print ("\n====================== ATIVIDADE 5 ========================")

'''Crie um programa que calcule o valor a ser pago pelo aluguel de um carro, 
  considerando que o valor da diária é R$ 60,00 e cada quilômetro percorrido custa R$ 0,15.'''

DiasAlugados = float(input("\nPor quantos dias o carro foi alugado?"))
KmPercorridos = float(input("Quantos quilômetros andou com o carro?"))
GastoTotal = DiasAlugados * 60.00 + KmPercorridos * 0.15

print(f"\nO gasto total do aluguel do carro ficará em {GastoTotal:2.2f} reais.")

print ("\n====================== ATIVIDADE 6 ========================")

'''Desenvolva um programa que calcule estatísticas de uma eleição com três candidatos (A, B e C).
   O programa deve mostrar o total de eleitores, o percentual de votos válidos em relação ao total de eleitores
   e o percentual de votos para cada candidato, além dos percentuais de votos nulos e em branco.'''

A = int(input("\nDigite quantos votos o candidato A obteve:"))
B = int(input("Digite quantos votos o candidato B obteve:"))
C = int(input("Digite quantos votos o candidato C obteve:"))
Nulos = int(input("Digite quantos votos nulos houveram:"))
Brancos = int(input("Digite quantos votos brancos:"))

totalEleitores = A + B + C + Nulos + Brancos
VotosValidos = ((A + B + C) / totalEleitores) * 100
VotosInvalidos = ((Nulos + Brancos) / totalEleitores) * 100
CandidatoA = (A / totalEleitores) * 100
CandidatoB = (B / totalEleitores) * 100
CandidatoC = (C / totalEleitores) * 100
VotosNulos = (Nulos / totalEleitores) * 100
VotosBrancos = (Brancos / totalEleitores) * 100

print("\nO total de eleitores foram de: ", totalEleitores)
print(f"Percentual de votos válidos: {VotosValidos:2.2f}")
print(f"Percentual de votos inválidos: {VotosInvalidos:2.2f}")
print(f"Percentual de votos para o candidato A: {CandidatoA:2.2f}")
print(f"Percentual de votos para o candidato B: {CandidatoB:2.2f}")
print(f"Percentual de votos para o candidato C: {CandidatoC:2.2f}")
print(f"Percentual de votos nulos: {VotosNulos:2.2f}")
print(f"Percentual de votos brancos: {VotosBrancos:2.2f}")

print ("\n====================== ATIVIDADE 7 ========================")

'''Crie um programa que converta uma distância fornecida em metros para outras unidades 
   (quilômetros, decímetros, centímetros e milímetros), formatando a saída com alinhamento.'''

DistanciaPercorrida = float(input("Digite quantos metros você percorreu:"))

km = DistanciaPercorrida / 1000
dm = DistanciaPercorrida * 10
cm = DistanciaPercorrida * 100
mm = DistanciaPercorrida * 1000

print(f"\nA distância que você percorreu foi de:"
      f"\n {km:2.2f} em quilômetros,"
      f"\n {dm:2.2f} em decímetros,"
      f"\n {cm:2.2f} em centímetros,"
      f"\n {mm:2.2f} em milímetros.")

print ("\n====================== ATIVIDADE 8 ========================")

'''Desenvolva um programa que troque os valores armazenados em duas variáveis
 A e B, mostrando os valores antes e depois da troca.'''

A = float(input("\nDigite o valor da variável A:"))
B = float(input("Digite o valor da variável B:"))

A, B = B, A

print(f"\nValor alterado entre as variáveis:"
      f"\n A = {A}"
      f"\n B = {B}")

print ("\n====================== ATIVIDADE 9 ========================")

'''Crie um programa que calcule o valor de desconto e o preço final de uma mercadoria,
 a partir do preço original e do percentual de desconto informados pelo usuário.'''

ValorMercadoria = float(input("\nDigite o preço da mercadoria: R$"))
PercentualDesconto = float(input("Digite o percentual de desconto:"))

CalculoDesconto = ValorMercadoria * (PercentualDesconto / 100)
DescontoTotal = ValorMercadoria - CalculoDesconto

print(f"\nO valor a ser pago com {PercentualDesconto}% ({CalculoDesconto} reais) é de {DescontoTotal:2.2f} reais")

print ("\n====================== ATIVIDADE 10 ========================")

'''Desenvolva um programa que solicite um número inteiro ao usuário e mostre seu antecessor e sucessor.'''

NumeroInteiro = int(input("\nDigite um número inteiro:"))

Antecessor = NumeroInteiro -1
Sucessor = NumeroInteiro +1

print(f"O número antecessor do número digitado é {Antecessor}, o sucessor é {Sucessor}.")








