# Funções para as operações matemáticas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro! Divisão por zero não é permitida."
    else:
        return a / b

# Função para exibir o menu
def exibir_menu():
    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

# Loop principal do programa
while True:
    exibir_menu()
    escolha = input("Digite o número da operação desejada: ")

    if escolha == '0':
        print("Obrigado por usar a calculadora. Encerrando o programa.")
        break
    elif escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print("Resultado: ", soma(num1, num2))
        elif escolha == '2':
            print("Resultado: ", subtracao(num1, num2))
        elif escolha == '3':
            print("Resultado: ", multiplicacao(num1, num2))
        elif escolha == '4':
            print("Resultado: ", divisao(num1, num2))
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
