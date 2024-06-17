def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    else:
        return a / b
    
def digiteNumero():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1,num2

def main():
    while True:
        print("\nEscolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        opcao = input("Digite sua opção: ")      

        if opcao == '1':
            num1, num2 = digiteNumero()
            print("Resultado:", soma(num1, num2))
        elif opcao == '2':
            num1, num2 = digiteNumero()
            print("Resultado:", subtracao(num1, num2))
        elif opcao == '3':
            num1, num2 = digiteNumero()
            print("Resultado:", multiplicacao(num1, num2))
        elif opcao == '4':
            num1, num2 = digiteNumero()
            print("Resultado:", divisao(num1, num2))
        elif opcao == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, digite 1, 2, 3, 4 ou 5.")

main()








