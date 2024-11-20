import random
import os


def limpar_tela():
    """Função para limpar a tela"""
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    """Função de apresentação para escolher entre gerar ou validar CPF"""
    while True:
        limpar_tela()
        print("Bem-vindo ao Gerador e Validador de CPF!")
        print("Escolha uma opção:")
        print("1 - Gerar CPF")
        print("2 - Validar CPF")
        print("0 - Sair")
        opcao = input("Opção: ")
        if opcao == "1":
            cpf_gerado = gerar_cpf()
            print(f"CPF Gerado: {cpf_gerado}")
            input("Pressione Enter para continuar...")
        elif opcao == "2":
            validar_cpf()
            input("Pressione Enter para continuar...")
        elif opcao == "0":
            print("Obrigado por Usar nosso sistema!")
            break
        else:
            print("Opção inválida! Por favor, escolha 1, 2 ou 0.")
            input("Pressione Enter para continuar...")


def gerar_nove_digitos():
    """Gera os primeiros nove dígitos do CPF"""
    nove_digitos = "".join([str(random.randint(0, 9)) for _ in range(9)])
    return nove_digitos


def calcular_digito_verificador(digitos, peso_inicial):
    """Calcula os dígitos verificadores do CPF"""
    soma = 0
    peso = peso_inicial
    for numero in digitos:
        soma += int(numero) * peso
        peso -= 1
    digito = (soma * 10) % 11
    return digito if digito < 10 else 0


def gerar_cpf():
    """Gera um CPF válido"""
    nove_digitos = gerar_nove_digitos()
    digito_1 = calcular_digito_verificador(nove_digitos, 10)
    dez_digitos = nove_digitos + str(digito_1)
    digito_2 = calcular_digito_verificador(dez_digitos, 11)
    cpf = dez_digitos + str(digito_2)
    return cpf


def validar_estrutura(cpf):
    """Valida a estrutura básica do CPF"""
    if len(cpf) != 11:
        print("Erro: O CPF deve ter 11 dígitos!")
        return False
    if not cpf.isdigit():
        print("Erro: O CPF deve conter apenas números, ou no formato xxx.xxx.xxx-xx")
        return False
    if len(set(cpf)) == 1:
        print("Erro: CPF inválido - todos os números são iguais!")
        return False
    return True


def verificar_cpf(cpf):
    """Verifica se o CPF é válido"""
    nove_digitos = cpf[:9]
    digito1 = calcular_digito_verificador(nove_digitos, 10)
    nove_digitos_mais_digito1 = nove_digitos + str(digito1)
    digito2 = calcular_digito_verificador(nove_digitos_mais_digito1, 11)
    cpf_calculado = f"{nove_digitos}{digito1}{digito2}"
    return cpf == cpf_calculado


def validar_cpf():
    """Função principal para validar o CPF"""
    cpf = input("Digite o CPF: ").replace(".", "").replace("-", "")
    if validar_estrutura(cpf):
        if verificar_cpf(cpf):
            print(f"O CPF {cpf} é válido!")
        else:
            print(f"O CPF {cpf} é inválido!")


# Executa o programa
if __name__ == "__main__":
    menu()
