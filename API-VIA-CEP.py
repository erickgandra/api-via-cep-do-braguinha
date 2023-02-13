import requests
def main():
    print('----API VIA CEP----')
# Pedindo o CEP para o usuario
    cep_input = input("Digite o CEP para consulta: ")
    while len(cep_input)!=8:
        print("A quantidade de digitos digitada é inválida")
        cep_input = input("Digite o CEP novamente: ")

        
    request = requests.get("https://viacep.com.br/ws/{}/json/".format(cep_input))
    adress_data = request.json()
# realiza uma busca no api via cep, caso seja satisfeita a condição, rodar o comando
    if "erro" not in adress_data:
        print('CEP: {}' .format(adress_data['cep']))
        print('Logradouro: {}' .format(adress_data['logradouro']))
        print('Complemento: {}' .format(adress_data['complemento']))
        print('Bairro: {}' .format(adress_data['bairro']))
        print('Cidade: {}' .format(adress_data['localidade']))
        print('Estado: {}' .format(adress_data['uf']))
# se nao for satisfeito a condição, vai dar mensagem de erro
    else:
        print(' {}:CEP INVÁLIDO!'.format(cep_input))
        print("--------------------------")
    option = int(input("Deseja realizar outra busca? \n 1- SIM \n 2- SAIR: "))

    if option == 1:
        main()
    else:
        print("Saindo.....")

if __name__ == "__main__":
    main()
