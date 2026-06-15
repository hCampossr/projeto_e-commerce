# 🛒 Henrique Shop - Simulador de E-commerce em Python

O **Henrique Shop** é um sistema de e-commerce baseado em terminal desenvolvido inteiramente em Python. O projeto simula as principais operações de uma loja virtual real, aplicando conceitos fundamentais de lógica de programação estruturada, manipulação de coleções (dicionários e listas) e persistência de dados em memória.

## 🚀 Funcionalidades

O sistema conta com um menu interativo que permite as seguintes ações:

1. **Ver Catálogo:** Exibe todos os produtos disponíveis na loja, detalhando nome, preço, categoria e quantidade em estoque.
2. **Buscar Produto:** Permite pesquisar itens específicos por nome ou categoria.
3. **Adicionar ao Carrinho:** Adiciona itens informando a quantidade desejada, contando com validação em tempo real do estoque disponível.
4. **Ver Carrinho:** Exibe a lista de produtos escolhidos, calcula o subtotal e o valor total (com ou sem a aplicação de cupons).
5. **Remover do Carrinho:** Permite diminuir a quantidade de um item no carrinho ou removê-lo completamente de forma dinâmica.
6. **Aplicar Cupom de Desconto:** Valida cupons promocionais específicos para conceder descontos sobre o valor total do carrinho.
7. **Finalizar Pedido:** Conclui a compra, atualiza permanentemente a quantidade dos produtos no estoque da loja e reseta o carrinho para uma nova sessão.

## 🎟️ Cupons de Desconto Disponíveis

O sistema aceita três cupons promocionais (não cumulativos):
* `HENRIQUE10`: Garante **10% de desconto** no valor total.
* `PUCTECH20`: Garante **20% de desconto** no valor total.
* `LOJA15`: Garante **15% de desconto** no valor total.
