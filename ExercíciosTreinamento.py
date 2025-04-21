print ("\n====================== ATIVIDADE 1 ========================")

'''Escreva um programa que converta um valor em Reais (R$) para Dólares e Euros.
   Peça ao usuário para inserir o valor em Reais e use as seguintes taxas de câmbio:
   1 BRL = 0,17 USD e 1 BRL = 0,15 EUR. Exiba os resultados com 2 casas decimais usando
   pelo menos dois métodos diferentes de formatação.'''

ValorUS = 0.17
ValorEU = 0.15

ValorReal = float(input("\nInsira o valor em REAL (R$) que você queira converter: "))
TipoMoeda = input("Digite a moeda que queira converter, DÓLAR ou EURO: ")

ConversaoUS = ValorReal * ValorUS
ConversaoEU = ValorReal * ValorEU

if TipoMoeda.upper() == "DÓLAR":
    print(f"\nO valor após a conversão é de: {ConversaoUS:2.2f} dólares.")
elif TipoMoeda.upper() == "EURO":
    print(f"O valor a ser pago pela conversão é de: {ConversaoEU:2.2f} euros.")
else:
    print("Moeda não reconhecida. Tente novamente.")

print ("\n====================== ATIVIDADE 2 ========================")

'''Crie um programa que peça ao usuário para inserir seu nome completo. Em seguida, exiba:
   (1) O número total de caracteres no nome (incluindo espaços)
   (2)O nome em letras maiúsculas
   (3) O nome em letras minúsculas
   (4) Apenas o primeiro nome
   (5) O nome com todas as letras 'a' substituídas por '@'''

NomeCompleto = input("\nDigite seu nome completo: ")

PrimeiroNome = NomeCompleto.split()[0]
NomeModificado = NomeCompleto.replace('A', '@').replace( 'a', '@')
print(f"Quantidade de caracteres no nome: {len(NomeCompleto)}")
print (f"Nome completo com letras maiúsculas: {NomeCompleto.upper()}")
print (f"Nome completo com letras minúsculas: {NomeCompleto.lower()}")
print (f"Apenas o primeiro nome: {PrimeiroNome}")
print (f"Nome modificado com @: {NomeModificado}")

print ("\n====================== ATIVIDADE 3 ========================")

'''Escreva um programa que peça ao usuário para inserir um número de segundos.
   Converta esse tempo para horas, minutos e segundos restantes, e exiba o resultado usando
   formatação de strings. Por exemplo, 3661 segundos devem ser exibidos como
   "1 hora, 1 minuto e 1 segundo".'''

SegundosTotal = int(input("\nDigite o número de segundos: "))

Horas = SegundosTotal // 3600
SegundosRestante = SegundosTotal % 3600
Minutos = SegundosRestante //60
Segundos = SegundosRestante % 3600

if Horas == 1:
    TextoHoras = "1 hora"
else:
    TextoHoras = f"{Horas}"

if Minutos == 1:
    TextoMinutos = "1 minuto"
else:
    TextoMinutos = f"{Minutos}"

if Segundos == 1:
    TextoSegundos = "1 segundo"
else:
    TextoSegundos = f"{Segundos}"

print (f"O tempo convertido é: {TextoHoras} horas, {TextoMinutos} minutos, {TextoSegundos} segundos.")

print ("\n====================== ATIVIDADE 4 ========================")

'''Escreva um código que calcule e imprima a hipotenusa de um triângulo retângulo, 
   com 2 casas decimais, cujos catetos serão entradas do usuário. Note que a raiz 
   quadrada de um numero X pode ser conseguida através de um potenciação 
   de X elevado 0.5 '''

A = int(input("\nDigite o valor do cateto A: "))
B = int(input("Digite o valor do cateto B: "))

Calculo = ((A**2) + (B**2))**0.5

print (f"A hipotenusa do triângulo retângulo é: {Calculo:2.2f}")

print ("\n====================== ATIVIDADE 5 ========================")

'''Escreva um programa que ajude a dividir uma conta de restaurante. Peça ao usuário para inserir:
   (1) O valor total da conta
   (2) O número de pessoas dividindo a conta
   (3) A porcentagem de gorjeta (por exemplo, 10 para 10%)
   Calcule quanto cada pessoa deve pagar, incluindo a gorjeta, e exiba o resultado com 2 casas decimais.'''

ValorConta = float(input("\nDigite o valor total da conta: "))
PessoasDividindo = int(input("Digite quantas pessoas estão dividindo a conta: "))
PorcentagemGorjeta = int(input("Digite a porcentagem da gorjeta ou taxa de serviço: "))

ValorPorcentagem = ValorConta * (PorcentagemGorjeta / 100)
ValorTotal = ValorConta + ValorPorcentagem
ValorDividido = ValorTotal / PessoasDividindo

print (f"O valor a ser pago por cada pessoa é de: {ValorDividido:2.2f} reais")

print ("\n====================== ATIVIDADE 6 ========================")

'''Solicite ao usuário um número inteiro. Gerando e exibindo a tabuada desse número de 1 a 10,
   formatada de forma legível.'''

NumeroTabuada = int(input("\nDigite um número inteiro de 0 a 10 para ver sua tabuada: "))

for i in range(0,11):
    resultado = NumeroTabuada * i
    print(f"Tabuada do número escolhido: {NumeroTabuada} x {i} = {resultado}")

print ("\n====================== ATIVIDADE 7 ========================")

'''Escreva um programa que calcule a distância entre dois pontos em um plano 2D.
   Peça ao usuário para inserir as coordenadas (x1, y1) e (x2, y2), e calcule a distância
   usando a fórmula: d = √[(x2-x1)² + (y2-y1)²]. Exiba o resultado com 3 casas decimais.'''

CoordenadaX1 = float(input("\nDigite a coordenada x1: "))
CoordenadaY1 = float(input("Digite a coordenada y1: "))
CoordenadaX2 = float(input("Digite a coordenada x2: "))
CoordenadaY2 = float(input("Digite a coordenada y2: "))

PassosFormula = (CoordenadaX2 - CoordenadaX1)**2
PassosFormula1 = (CoordenadaY2 - CoordenadaY1)**2
PassosFormula3 = PassosFormula + PassosFormula1
PassosFormula4 = PassosFormula3**0.5

print(f"A distância entre as coordenadas é de: {PassosFormula4:3.3f}")

print ("\n====================== ATIVIDADE 8 ========================")

'''Crie um programa que calcule a nota final de um aluno. Peça ao usuário para inserir três notas de provas
   (0-10), e calcule a média ponderada onde a primeira prova vale 20%, a segunda prova vale 30% e a
   terceira prova vale 50%. Exiba a nota final com 1 casa decimal e uma mensagem indicando se o aluno foi
   aprovado (nota ≥ 6,0) ou reprovado.'''

Prova1 = float(input("\nDigite a primeira nota: "))
Prova2 = float(input("Digite a segunda nota: "))
Prova3 = float(input("Digite a terceira nota: "))

PorcentagemProva1 = 20
PorcentagemProva2 = 30
PorcentagemProva3 = 50

CalculoPorcentagem1 = Prova1 * (PorcentagemProva1 / 100)
CalculoPorcentagem2 = Prova2 * (PorcentagemProva2 / 100)
CalculoPorcentagem3 = Prova3 * (PorcentagemProva3 / 100)

MediaProvas = (CalculoPorcentagem1 + CalculoPorcentagem2 + CalculoPorcentagem3)

if MediaProvas >= 6.0:
    print(f"A média obtida nas três provas foi de: {MediaProvas:1.1f}.")
    print("Aprovado.")
else:
    print(f"\nA média obtida nas três provas foi de: {MediaProvas:1.1f}.")
    print("Reprovado.")

print ("\n====================== ATIVIDADE 9 ========================")

'''Escreva um programa que simule um pequeno carrinho de compras.
   Peça ao usuário para inserir o nome e o preço de 3 produtos, e calcule e exiba:
   (1) A lista de produtos e seus preços
   (2) O subtotal
   (3) Imposto (15% do subtotal)
   (4) Total (subtotal + imposto)
   Use formatação adequada para alinhar todos os valores e símbolos de moeda.'''

Produto1 = input("\nDigite o nome do produto 1: ")
PrecoProduto1 = float(input("Digite o preço do produto 1: "))
Produto2 = input("Digite o nome do produto 2: ")
PrecoProduto2 = float(input("Digite o preço do produto 2: "))
Produto3 = input("Digite o nome do produto 3: ")
PrecoProduto3 = float(input("Digite o preço do produto 3: "))

Imposto = 15
SubTotal = PrecoProduto1 + PrecoProduto2 + PrecoProduto3
CalculoImposto = SubTotal * (Imposto / 100)
TotalCompra = SubTotal + CalculoImposto

print("\n====================== RECIBO ========================")
print(f"{Produto1: <40} R${PrecoProduto1:2.2f}.")
print(f"{Produto2: <40} R${PrecoProduto2:2.2f}.")
print(f"{Produto3: <40} R${PrecoProduto3:2.2f}.")

print("\n====================== TOTAL ========================")
print(f"R$: {SubTotal:2.2f}.")
print("Imposto Municipal: 5%.")
print("Imposto Estadual: 5%.")
print("Imposto Federal: 5%.")
print(f"Preço final: R$ {TotalCompra}.")

print ("\n====================== ATIVIDADE 10 ========================")

'''Escreva um programa que peça ao usuário para inserir uma temperatura em Fahrenheit, e converta-a
   para Celsius e Kelvin usando as fórmulas:
   
   C = (F - 32) * 5/9
   K = C + 273,15

   Exiba ambos os resultados com 1 casa decimal usando diferentes métodos de
   formatação mostrados no código de exemplo.'''

Fahrenheit = float(input("\nDigite uma temperatura em Fahrenheit: "))

Celsius = (Fahrenheit - 32) * 5/9
Kelvin = (Celsius + 273.15)

print("A conversão de Fahrenheit para Celsius e Kelvin é de:"
      f"\n {Celsius:1.1f} graus."
      f"\n {Kelvin:1.1f} kelvin.")

