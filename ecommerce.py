def ver_catalogo():
    for produto in catalogo.values():
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Categoria: {produto['categoria']}")
        print("-" * 20)

def buscar_produto():
    busca  = input("Busque o produto (nome ou categoria): \n")
    achou = False
    for produto in catalogo.values():
        if (produto['nome'] == busca or produto['categoria'] == busca):
            print(f"Nome: {produto['nome']}\n"
                  f"Preço: R${produto['preco']:.2f}\n"
                  f"Categoria: {produto['categoria']}\n")
            achou = True
    if achou == False:
        print("Produto não disponível em estoque")

def add_carrinho():
    adicionar = input("Nome do produto para adicionar: \n")
    qtde = int(input("Quantidade: "))
    achou = False

    for produto in catalogo.values():
        if (produto['nome'].lower() == adicionar.lower()):
            achou = True

            if qtde <= produto['quantidade']:
                carrinho[produto['nome']] = qtde
            print(f"{qtde}x {produto['nome']} adicionado ao carrinho")
        else:
            print("Estoque insuficiente")

        break
    if achou == False:
        print("Produto não disponível em estoque")



catalogo = {
    "Produto1": {"nome": "Jaqueta", "preco": 279.79, "categoria": "Frio", "quantidade": 10},
    "Produto2": {"nome": "Calça", "preco": 199.99, "categoria": "Frio", "quantidade": 15},
    "Produto3": {"nome": "Bermuda", "preco": 129.29, "categoria": "Calor", "quantidade": 15},
    "Produto4": {"nome": "Camiseta", "preco": 89.90, "categoria": "Calor", "quantidade": 20},
    "Produto5": {"nome": "Corrente", "preco": 89.90, "categoria": "Acessorios", "quantidade": 25},
    "Produto6": {"nome": "Pulseira", "preco": 79.99, "categoria": "Acessorios", "quantidade": 15}
}

carrinho = {}

print("==== Bem-vindo ao Henrique Shop ====\n\n")
menu_opcao = int(input("O QUE VOCE DESEJA FAZER?\n"
      "1 - Ver catalogo\n"
      "2- Buscar produto\n"
      "3 - Adicionar produto ao carrinho\n"
      "4 - Remover produto do carrinho\n"
      "5 - Ver valor total do carrinho\n"
      "6 - Aplicar cupom de desconto\n"
      "7 - Finalizar pedido\n\n"
      "0 - Sair\n"))

if menu_opcao == 1:
    ver_catalogo()
elif menu_opcao == 2:
    buscar_produto()
elif menu_opcao == 3:
    add_carrinho()
