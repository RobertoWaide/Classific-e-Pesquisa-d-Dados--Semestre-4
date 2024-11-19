class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = {i: [] for i in range(size)}

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Adiciona um par chave-valor no vetor correspondente
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # Atualiza o valor caso a chave já exista
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Retorna None caso a chave não seja encontrada

    def remove(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return True
        return False  # Retorna False caso a chave não seja encontrada

    def display(self):
        for index, items in self.table.items():
            print(f"Index {index}: {items}")

# Exemplo de uso

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
