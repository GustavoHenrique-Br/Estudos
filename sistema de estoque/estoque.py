import json
nome_arquivo = 'db.json'

try:
    with open('db.json', 'r') as arquivo:
        dict_produtos = json.load(arquivo)
except FileNotFoundError:
    dict_produtos = []
while True:
    print("\n---> Sistema de Estoque <---")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Salvar e Sair")
    try:
        escolha = int(input("Escolha uma opcao: "))
        if escolha == 1:
            nome_produto = input("Qual o nome do produto: ").lower()
            preco_produto = float(input("Qual o valor do produto: "))
            
            novo_produto = {'nome': nome_produto, 'preco': preco_produto}
            dict_produtos.append(novo_produto)
            print(f"{nome_produto} adicionado!")
        elif escolha == 2:
            print("--- Lista ---")
            if not dict_produtos:
                print("Nenhum produto cadastrado")
            else:
                for produto in dict_produtos:
                        print(f"Nome: {produto['nome']} | R${produto['preco']: .2f}")
        elif escolha == 3:
            print("Salvando os dados...")
            break
        else:
            print("Opcao inválida")
    except ValueError:
        print("Digite um numero válido")

with open('db.json', 'w') as arquivo:
    json.dump(dict_produtos, arquivo, indent=4)