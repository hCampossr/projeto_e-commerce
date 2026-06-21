class Produto:
    def __init__(self, nome, preco, categoria, quantity):
        self.nome = nome
        self.__preco = preco  # Atributo privado
        self.categoria = categoria
        self.__quantidade = quantity  # Atributo privado

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