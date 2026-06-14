def ver_catalogo():
    for produto in catalogo.values():
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Categoria: {produto['categoria']}")
        print("-" * 20)


catalogo = {
    "Produto1": {"nome": "Jaqueta", "preco": 279.79, "categoria": "frio", "quantidade": 10},
    "Produto2": {"nome": "Calça", "preco": 199.99, "categoria": "frio", "quantidade": 15},
    "Produto3": {"nome": "Bermuda", "preco": 129.29, "categoria": "calor", "quantidade": 15},
    "Produto4": {"nome": "Camiseta", "preco": 89.90, "categoria": "calor", "quantidade": 20},
    "Produto5": {"nome": "Corrente", "preco": 89.90, "categoria": "acessorios", "quantidade": 25},
    "Produto6": {"nome": "Pulseira", "preco": 79.99, "categoria": "acessorios", "quantidade": 15}
}

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
