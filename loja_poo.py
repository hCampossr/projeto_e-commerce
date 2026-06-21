class Produto:
    def __init__(self, nome, preco, categoria, quantity):
        self.nome = nome
        self.__preco = preco
        self.categoria = categoria
        self.__quantidade = quantity

    @property
    def preco(self):
        return self.__preco

    @property
    def quantidade(self):
        return self.__quantidade

    def reduzir_estoque(self, qtde):
        if qtde <= self.__quantidade:
            self.__quantidade -= qtde
            return True
        return False

    def incrementar_estoque(self, qtde):
        self.__quantidade += qtde

    def __str__(self):
        return (f"Nome: {self.nome} | "
                f"Preço: R${self.__preco:.2f} | "
                f"Categoria: {self.categoria} | "
                f"Estoque: {self.__quantidade}")

    def __repr__(self):
        return f"Produto('{self.nome}', {self.__preco}, '{self.categoria}', {self.__quantidade})"


class Desconto:
    def __init__(self, codigo, porcentagem):
        self.codigo = codigo.upper()
        self.porcentagem = porcentagem

    def calcular(self, valor_total):
        return valor_total * (1 - self.porcentagem)


class CupomFixo(Desconto):
    def __str__(self):
        return f"Cupom: {self.codigo} | Desconto: {self.porcentagem * 100:.0f}%"


class Carrinho:
    def __init__(self):
        self.itens = {}
        self.cupom_aplicado = None

    def adicionar(self, produto, qtde):
        if qtde <= produto.quantidade:
            if produto in self.itens:
                self.itens[produto] += qtde
            else:
                self.itens[produto] = qtde
            print(f"{qtde}x {produto.nome} adicionado ao carrinho com sucesso!")
            return True
        print(f"Estoque insuficiente! Apenas {produto.quantidade} unidades disponíveis.")
        return False

    def remover(self, produto, qtde):
        if produto in self.itens:
            if qtde >= self.itens[produto]:
                del self.itens[produto]
                print(f"'{produto.nome}' foi totalmente removido do carrinho.")
            else:
                self.itens[produto] -= qtde
                print(f"{qtde}x '{produto.nome}' removidos do carrinho.")
        else:
            print("Este produto não está no seu carrinho.")

    def calcular_total(self):
        total = sum(prod.preco * qtde for prod, qtde in self.itens.items())

        if self.cupom_aplicado:
            total = self.cupom_aplicado.calcular(total)
        return total

    def limpar(self):
        self.itens = {}
        self.cupom_aplicado = None

    def __str__(self):
        if not self.itens:
            return "Seu carrinho está vazio."

        res = "\n==== ITENS NO CARRINHO ====\n"
        subtotal_sem_desconto = 0
        for prod, qtde in self.itens.items():
            sub = prod.preco * qtde
            subtotal_sem_desconto += sub
            res += f"- {prod.nome}: {qtde}x R${prod.preco:.2f} = R${sub:.2f}\n"
        res += "===========================\n"

        if self.cupom_aplicado:
            res += f"Subtotal: R${subtotal_sem_desconto:.2f}\n"
            res += f"Cupom Ativo: {self.cupom_aplicado.codigo}\n"

        res += f"TOTAL FINAL: R${self.calcular_total():.2f}\n"
        return res


class Pedido:
    def __init__(self, id_pedido, itens_comprados, total_pago):
        self.id_pedido = id_pedido
        self.itens_comprados = itens_comprados
        self.total_pago = total_pago

    def __str__(self):
        res = f"📦 RECOBIMENTO DO PEDIDO #{self.id_pedido}\n"
        res += "Produtos comprados:\n"
        for prod, qtde in self.itens_comprados.items():
            res += f"  - {prod.nome} ({qtde}x)\n"
        res += f"Valor total pago: R${self.total_pago:.2f}\n"
        res += "--------------------------------------"
        return res


class Loja:
    def __init__(self):
        self.catalogo = {}
        self.cupons = {}
        self.historico_pedidos = []
        self.carrinho_atual = Carrinho()
        self.__proximo_id_pedido = 1

    def cadastrar_produto(self, id_prod, produto):
        self.catalogo[id_prod] = produto

    def cadastrar_cupom(self, cupom):
        self.cupons[cupom.codigo] = cupom

    def buscar_produto(self, termo):
        achou = False
        termo = termo.lower()
        print("\n--- Resultado da Busca ---")
        for prod in self.catalogo.values():
            if termo in prod.nome.lower() or termo in prod.categoria.lower():
                print(prod)
                achou = True
        if not achou:
            print("Nenhum produto disponível em estoque com este nome ou categoria.")
        print("--------------------------")

    # AJUSTE 1: Método finalizar_pedido agora está no nível correto dentro da Loja
    def finalizar_pedido(self):
        if not self.carrinho_atual.itens:
            print("Seu carrinho está vazio. Adicione produtos antes de finalizar.")
            return

        print("\n--- Finalizando Pedido ---")
        for prod, qtde in self.carrinho_atual.itens.items():
            prod.reduzir_estoque(qtde)
            print(f"Baixa no estoque: {prod.nome} (-{qtde})")

        novo_pedido = Pedido(
            id_pedido=self.__proximo_id_pedido,
            itens_comprados=self.carrinho_atual.itens.copy(),
            total_pago=self.carrinho_atual.calcular_total()
        )
        self.historico_pedidos.append(novo_pedido)
        self.__proximo_id_pedido += 1

        print("\nPedido finalizado com sucesso no Henrique Shop! Volte sempre.")
        print(novo_pedido)

        self.carrinho_atual.limpar()


# AJUSTE 2: Função executar_sistema totalmente para fora das classes
def executar_sistema():
    minha_loja = Loja()

    minha_loja.cadastrar_produto(1, Produto("Camiseta Estampada", 59.90, "Roupas", 20))
    minha_loja.cadastrar_produto(2, Produto("Calça Jeans Slim", 120.00, "Roupas", 15))
    minha_loja.cadastrar_produto(3, Produto("Tênis Esportivo", 249.99, "Calçados", 8))
    minha_loja.cadastrar_produto(4, Produto("Meias Cano Curto", 15.50, "Acessórios", 50))

    minha_loja.cadastrar_cupom(CupomFixo("HENRIQUE10", 0.10))
    minha_loja.cadastrar_cupom(CupomFixo("SUPER20", 0.20))

    while True:
        print("\n=== HENRIQUE SHOP - VERSÃO POO ===")
        print("1. Listar Catálogo Completo")
        print("2. Buscar Produto por Nome/Categoria")
        print("3. Adicionar Produto ao Carrinho")
        print("4. Remover Produto do Carrinho")
        print("5. Ver Carrinho e Subtotal")
        print("6. Aplicar Cupom de Desconto")
        print("7. Finalizar Pedido")
        print("8. Ver Histórico de Pedidos Fechados")
        print("9. Sair do Sistema")