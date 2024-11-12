class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min_larger_node = self._get_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursive(node.right, min_larger_node.value)

        return node

    def _get_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def pre_order_traversal(self):
        return self._pre_order_recursive(self.root)

    def _pre_order_recursive(self, node):
        if node is None:
            return []
        return [node.value] + self._pre_order_recursive(node.left) + self._pre_order_recursive(node.right)

    def in_order_traversal(self):
        return self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        if node is None:
            return []
        return self._in_order_recursive(node.left) + [node.value] + self._in_order_recursive(node.right)

    def post_order_traversal(self):
        return self._post_order_recursive(self.root)

    def _post_order_recursive(self, node):
        if node is None:
            return []
        return self._post_order_recursive(node.left) + self._post_order_recursive(node.right) + [node.value]



def main():
    # Criando a árvore binária de busca
    bst = BinarySearchTree()
    
    while True:
        print("\nEscolha uma opção:")
        print("1 - Inserir um valor")
        print("2 - Buscar um valor")
        print("3 - Remover um valor")
        print("4 - Mostrar em pré-ordem")
        print("5 - Mostrar em ordem simétrica")
        print("6 - Mostrar em pós-ordem")
        print("7 - Sair")
        choice = input("\nOpção: ")

        if choice == "1":
            value = int(input("Digite o valor para inserir: "))
            bst.insert(value)
            print(f"Valor {value} inserido.")

        elif choice == "2":
            value = int(input("Digite o valor para buscar: "))
            result = bst.search(value)
            if result:
                print(f"\nValor [{value}] encontrado.")
            else:
                print(f"\nValor [{value}] não encontrado.")

        elif choice == "3":
            value = int(input("Digite o valor para remover: "))
            bst.delete(value)
            print(f"\nValor [{value}] removido se existia na árvore.")

        elif choice == "4":
            print("Percurso em pré-ordem:", bst.pre_order_traversal())

        elif choice == "5":
            print("Percurso em ordem simétrica:", bst.in_order_traversal())

        elif choice == "6":
            print("Percurso em pós-ordem:", bst.post_order_traversal())

        elif choice == "7":
            break

        else:
            print("Opção inválida.")

main()
