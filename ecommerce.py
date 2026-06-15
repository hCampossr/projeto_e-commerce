def ver_catalogo():
    for produto in catalogo.values():
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Quantidade: {produto['quantidade']}")
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

def ver_carrinho():
    if not carrinho:
        print("Carrinho vazio")
        return
    total = 0

    for produto_nome, qtde in carrinho.items():
        for produto_cat in catalogo.values():
            if produto_cat['nome'] == produto_nome:
                subtotal = produto_cat['preco'] * qtde
                total += subtotal
                print(f"- {produto_nome}: {qtde}x R${produto_cat['preco']:.2f} = R${subtotal:.2f}")
    if desconto < 1.0:
        total_com_desconto = total * desconto
        print(f"Subtotal: R${total:.2f}")
        print(f"TOTAL COM DESCONTO: R${total_com_desconto:.2f}\n")
    else:
        print(f"TOTAL: R${total:.2f}\n")

def delete_carrinho():
    if not carrinho:
        print("Seu carrinho esta vazio")
        return

    remover = input("Qual item voce deseja remover (nome)?\n")

    produto_encontrado = None
    for produto in carrinho.keys():
        if produto.lower() == remover.lower():
            produto_encontrado = produto
            break

    if produto_encontrado:
        qtde_remover = int(input(f"Quantos '{produto_encontrado} deseja remover?\n"))

        if qtde_remover >= carrinho[produto_encontrado]:
            del carrinho[produto_encontrado]
            print(f"{produto_encontrado} foi removido do carrinho.")
        else:
            carrinho[produto_encontrado] -= qtde_remover
            print(f"{qtde_remover}x '{produto_encontrado}' removidos.")
    else:
        print("Esse produto não está no seu carrinho.")

def aplicar_cupom():
    global desconto
    if not carrinho:
        print("Carrinho vazio. Não é possível adicionar cupom")
    incupom = input("Insira um cupom: ").upper()
    if incupom in cupom:
        if incupom == "HENRIQUE10":
            desconto = 0.90
            print("Cupom HENRIQUE10 aplicado com sucesso!")
        elif incupom == "PUCTECH20":
            desconto = 0.80
            print("Cupom PUCTECH20 aplicado com sucesso!")
        elif incupom == "LOJA15":
            desconto = 0.85
            print("Cupom LOJA15 aplicado com sucesso!")
    else:
        print("Cupom inválido ou expirado.")




catalogo = {
    "Produto1": {"nome": "Jaqueta", "preco": 279.79, "categoria": "Frio", "quantidade": 10},
    "Produto2": {"nome": "Calça", "preco": 199.99, "categoria": "Frio", "quantidade": 15},
    "Produto3": {"nome": "Bermuda", "preco": 129.29, "categoria": "Calor", "quantidade": 15},
    "Produto4": {"nome": "Camiseta", "preco": 89.90, "categoria": "Calor", "quantidade": 20},
    "Produto5": {"nome": "Corrente", "preco": 89.90, "categoria": "Acessorios", "quantidade": 25},
    "Produto6": {"nome": "Pulseira", "preco": 79.99, "categoria": "Acessorios", "quantidade": 15}
}

carrinho = {}
cupom = ["HENRIQUE10", "PUCTECH20", "LOJA15"]
desconto = 1.0

while True:
    print("==== Bem-vindo ao Henrique Shop ====\n\n")
    menu_opcao = int(input("O QUE VOCE DESEJA FAZER?\n"
          "1 - Ver catalogo\n"
          "2- Buscar produto\n"
          "3 - Adicionar produto ao carrinho\n"
          "4 - Ver carrinho\n"                 
          "5 - Remover produto do carrinho\n"
          "6 - Aplicar cupom de desconto\n"
          "7 - Finalizar pedido\n\n"
          "0 - Sair\n"))

    if menu_opcao == 1:
        ver_catalogo()
    elif menu_opcao == 2:
        buscar_produto()
    elif menu_opcao == 3:
        add_carrinho()
    elif menu_opcao == 4:
        ver_carrinho()
    elif menu_opcao == 5:
        delete_carrinho()
    elif menu_opcao == 6:
        aplicar_cupom()

    elif menu_opcao == 0:
        break
    else:
        print("Digite um numero valido")