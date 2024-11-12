class Produto:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

class NodoBST:
    def __init__(self, produto):
        self.produto = produto
        self.esquerda = None
        self.direita = None

class ArvoreBinariaDeBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, produto):
        if not self.raiz:
            self.raiz = NodoBST(produto)
        else:
            self._inserir_nodo(self.raiz, produto)

    def _inserir_nodo(self, nodo, produto):
        if produto.id < nodo.produto.id:
            if nodo.esquerda is None:
                nodo.esquerda = NodoBST(produto)
            else:
                self._inserir_nodo(nodo.esquerda, produto)
        elif produto.id > nodo.produto.id:
            if nodo.direita is None:
                nodo.direita = NodoBST(produto)
            else:
                self._inserir_nodo(nodo.direita, produto)

    def buscar(self, id):
        return self._buscar_nodo(self.raiz, id)

    def _buscar_nodo(self, nodo, id):
        if nodo is None or nodo.produto.id == id:
            return nodo.produto if nodo else None
        if id < nodo.produto.id:
            return self._buscar_nodo(nodo.esquerda, id)
        else:
            return self._buscar_nodo(nodo.direita, id)

    def remover(self, id):
        self.raiz = self._remover_nodo(self.raiz, id)

    def _remover_nodo(self, nodo, id):
        if nodo is None:
            return nodo
        if id < nodo.produto.id:
            nodo.esquerda = self._remover_nodo(nodo.esquerda, id)
        elif id > nodo.produto.id:
            nodo.direita = self._remover_nodo(nodo.direita, id)
        else:
            if nodo.esquerda is None:
                return nodo.direita
            elif nodo.direita is None:
                return nodo.esquerda

            menor_nodo = self._encontrar_menor(nodo.direita)
            nodo.produto = menor_nodo.produto
            nodo.direita = self._remover_nodo(nodo.direita, menor_nodo.produto.id)
        return nodo

    def _encontrar_menor(self, nodo):
        atual = nodo
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def listar_em_ordem(self):
        produtos = []
        self._in_order_traversal(self.raiz, produtos)
        return produtos

    def _in_order_traversal(self, nodo, produtos):
        if nodo is not None:
            self._in_order_traversal(nodo.esquerda, produtos)
            produtos.append(nodo.produto)
            self._in_order_traversal(nodo.direita, produtos)

def menu():
    arvore = ArvoreBinariaDeBusca()
    
    while True:
        print("\n--- Menu ---\n")
        print("1 - Inserir produto")
        print("2 - Buscar produto por ID")
        print("3 - Remover produto por ID")
        print("4 - Listar produtos em ordem crescente de ID")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                id = int(input("ID do produto: "))
                nome = input("Nome do produto: ")
                descricao = input("Descrição do produto: ")
                preco = float(input("Preço do produto: "))
                produto = Produto(id, nome, descricao, preco)
                arvore.inserir(produto)
                print("Produto inserido com sucesso!")
            except ValueError:
                print("Entrada inválida.\nTente novamente.")

        elif opcao == "2":
            try:
                id = int(input("ID do produto para buscar: "))
                produto = arvore.buscar(id)
                if produto:
                    print(f"Produto encontrado: Nome: {produto.nome}, Descrição: {produto.descricao}, Preço: {produto.preco}")
                else:
                    print("Produto não encontrado.")
            except ValueError:
                print("Entrada inválida.\nTente novamente.")

        elif opcao == "3":
            try:
                id = int(input("ID do produto para remover: "))
                arvore.remover(id)
                print(f"Produto [id{id}] removido se existente.")
            except ValueError:
                print("Entrada inválida.\nTente novamente.")

        elif opcao == "4":
            produtos_ordenados = arvore.listar_em_ordem()
            if produtos_ordenados:
                print("\nProdutos em ordem crescente de ID:")
                for produto in produtos_ordenados:
                    print(f"ID: {produto.id}, Nome: {produto.nome}, Descrição: {produto.descricao}, Preço: {produto.preco}")
            else:
                print("Nenhum produto encontrado.")

        elif opcao == "5":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()
