from datetime import datetime

def ler_valor_nao_vazio(nome_variavel):
    valor_lido = input(f'Entre com o valor para {nome_variavel} do animal: ')
    while valor_lido == '':
        print(f'O valor para {nome_variavel} não pode ser vazio!')
        valor_lido = input(f'Entre com o valor para {nome_variavel} do animal: ')
    return valor_lido

def ler_animal():
    nome = ler_valor_nao_vazio('nome')
    especie = ler_valor_nao_vazio('espécie')
    dataNascimentoString = input('Entre com a data de nascimento: ')
    dataNascimento = datetime.strptime(dataNascimentoString, "%d/%m/%Y")
    tutor = ler_valor_nao_vazio('nome do tutor')

    animal = {
        'nome': nome,
        'especie': especie,
        'dataNascimento': dataNascimento,
        'tutor': tutor
    }

    return animal

def imprimir_animal(animal):
    print(f"Nome:\t\t{animal['nome']}")
    print(f"Espécie:\t{animal['especie']}")
    print(f"Data:\t\t{animal['dataNascimento'].strftime('%d/%m/%Y')}")
    print(f"Tutor:\t\t{animal['tutor']}")

meu_bixinho = ler_animal()
meu_outro_bixinho = ler_animal()
imprimir_animal(meu_bixinho)
imprimir_animal(meu_outro_bixinho)