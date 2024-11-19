class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)  
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value  
                    return
                if current.next is None:  
                    break
                current = current.next
            current.next = Node(key, value) 

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value 
            current = current.next
        return None  

    def remove(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True  
            prev = current
            current = current.next
        return False  

    def display(self):
        for i, node in enumerate(self.table):
            print(f"Index {i}:", end=" ")
            current = node
            while current:
                print(f"({current.key}, {current.value}) ->", end=" ")
                current = current.next
            print("None")

def main():
    htable = HashTable(10)
    
    while True:
        i = input("\n1-Inserir\n2-Mostrar\n3-Buscar\n4-Remover\n5-Exemplo\n-")
        if i == "1":
            nome = input("\nDigite a chave: ")
            numero = int(input("Digite o valor: "))
            htable.insert(nome, numero)
        elif i == "2":
            htable.display()
        elif i == "3":
            nome = input("\nDigite a chave para busca: ")
            print(f"\nBusca por {nome}:", htable.search(nome))
        elif i == "4":
            nome = input("\nDigite a chave para remover: ")
            htable.remove(nome)
        elif i == "5":
            htable.insert("apple", 10)
            htable.insert("banana", 20)
            htable.insert("orange", 30)

            htable.display()

            print("\nBusca por 'apple':", htable.search("apple"),"\n")
            htable.remove("banana")
            htable.display()

main()
