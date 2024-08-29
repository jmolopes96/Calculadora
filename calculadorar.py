print("Seja bem vindo a calculadora do jaomartelo :>")

def escolher_operacao():
    print("""
    Escolha a operacao desejada
    1 - adicao
    2 - subtracao
    3 - multiplicacao
    4 - divisao
    """)
    operacao = input("Escolha a operacao desejada: ")
    return operacao

def escolher_numeros():
    escolher = input("escolha um numero: ")
    print("o numero escolhido foi: " + escolher)
    return escolher

def calcular(num1, num2, op):
    if op == "1":
        return num1 + num2
    if op == "2":
        return num1 - num2
    if op == "3":
        return num1 * num2
    if op == "4":
        return num1 / num2

# operacao = escolher_operacao()
# numero1 = escolher_numeros()
# numero2 = escolher_numeros()
# print(calcular(int(numero1),int(numero2),operacao))

continuar = 'S'
while continuar == 'S':
    operacao = escolher_operacao()
    numero1 = escolher_numeros()
    numero2 = escolher_numeros()
    print(calcular(float(numero1),float(numero2),operacao))
    continuar = input("gostaria de continuar com a calculadora?[S/N] ")