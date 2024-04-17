# Projeto completo de Calculadora
# @author Sandees
# TIPOS DISPONIVEIS DE CALCULO: DIVISÃO, MULTIPLICAÇÃO, ADIÇÃO.
# Em String

# Importando o getpass para esconder as senhas do usuário.
from getpass import getpass

# Definindo em String as mensagens do input(pergunta ao usuário)
first_name_user = '\n Qual o seu nome? '
password_user = "\n Qual sua senha? Sua senha está segura em nossa base de dados e ficará segura. \nLembre-se, utilizamos uma estrutura totalmente criptografada para melhorar sua segurança. \n Digite sua senha: "
email_user_lang = "\n Digite o seu email: "
# Mensagens ao cadastrar
sucess_login = '\nNome cadastrado com sucesso.'
password_sucess = '\nSua senha foi cadastrada com sucesso.'
email_sucess = '\nO seu e-mail foi cadastrado com sucesso.'

message = input('\n Olá cliente, vamos começar a iniciar um cadastro básico para utilizarmos a calculadora.\n * Escreva "Continuar" para prosseguir com cadastro ou "Seguir" direto a calculadora. \n')
if message == "Continuar":
    print("Certo! Vamos começar pelo seu nome! Tudo certo?")

    # Criando o cadastro
    first = str (input(first_name_user))
    print(sucess_login)
    
    password = getpass(password_user)
    print(password_sucess)

    email = input(email_user_lang)
    print(email_sucess)

    # Informação do usuário final
    print("\n Com base do seu cadastro seu nome é", first + "\nSenha cadastrada: ", password + "\nE-mail cadastrado: ", email)
    # Prosseguindo para calculadora.
    print("\n" + "Show, {} vamos prosseguir a calculadora.".format(first))
    # print("Show, vamos prosseguir a calculadora.") <--- formato normal. Sem usar o format.

    # Selecionando o tipo de calculo.
    # Tipos disponíveis: Divisão, Multiplicação, Adição.
while True:
    message = input("\n Vamos começar buscando a forma que você quer trabalhar em nossa calculadora, certo? \n \n * Tipos de calculos disponíveis: \n \n * Adição \n * Multiplicação \n * Divisão \n \n O sistema automaticamente irá repetir a ação até que você cancele.\n ")  
    # Digitando o numero para o calculo
    test = int(input("Digite o primeiro numero: "))
    test_2 = int(input("Digite o segundo numero: "))

    if message == "Adição":
        print("\n" + "Resultado final da adição: {}"
        .format(test + test_2))
        # print("Resultado do calculo: ", test + test_2) <--- formato normal. Sem precisar usar o 'format'.
    elif message == "Multiplicação":
        print("\n" + "Resultado final da multiplicação: {}"
        .format( test * test_2))
        # print("Resultado do calculo: ", test * test_2) <--- formato normal. Sem precisar usar o 'format'.
    elif message == "Divisão":
        # print("Resultado do calculo: ", test / test_2) <--- formato normal. Sem precisar usar o 'format'.
        print("\n" + " Resultado final da divisão: {}"
        .format( test / test_2)) 
    else: 
        print("Ocorreu um erro ao calcular.")

# Seguindo direto para calculadora       
    if message == "Seguir":
    # Selecionando o tipo de calculo.
    # Tipos disponíveis: Divisão, Multiplicação, Adição.
     message2 = input("Vamos começar buscando a forma que você quer trabalhar em nossa calculadora, certo? \n * Tipos de calculos disponíveis: \n \n * Adição \n * Multiplicação \n * Divisão \n \n")
    # Digitando o numero para o calculo
     test = int(input("Digite o primeiro numero: "))
     test_2 = int(input("Digite o segundo numero: "))

     if message2 == "Adição":
        print("\n" +"Resultado do calculo: {}"
        .format(test + test_2))
        # print("Resultado do calculo: ", test + test_2) <--- formato normal. Sem precisar usar o 'format'.
     elif message2 == "Multiplicação":
        print("\n" +"Resultado do calculo: {}"
        .format(test * test_2))
        # print("Resultado do calculo: ", test * test_2) <--- formato normal. Sem precisar usar o 'format'.
     elif message2 == "Divisão":
        print("\n" +"Resultado do calculo: {}"
        .format(test / test_2))
        # print("Resultado do calculo: ", test / test_2) <--- formato normal. Sem precisar usar o 'format'. 
     elif message2 == "Fração":
        print("") 
     else:
        print("Ocorreu um erro ao calcular.")    

    
