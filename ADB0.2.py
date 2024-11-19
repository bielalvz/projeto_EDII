class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def criar_arvore(self):
        self.raiz = None
        print("Árvore criada!")

    def exibir_arvore(self, no):
        if no:
            self.exibir_arvore(no.esquerda)
            print(no.valor, end=" ")
            self.exibir_arvore(no.direita)

    def buscar(self, no, valor):
        if no is None or no.valor == valor:
            return no
        if valor < no.valor:
            return self.buscar(no.esquerda, valor)
        return self.buscar(no.direita, valor)

    def inserir(self, no, valor):
        if no is None:
            return No(valor)
        if valor < no.valor:
            no.esquerda = self.inserir(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self.inserir(no.direita, valor)
        return no

    def remover(self, no, valor):
        if no is None:
            return no
        if valor < no.valor:
            no.esquerda = self.remover(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self.remover(no.direita, valor)
        else:
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            no.valor = self.valor_minimo(no.direita)
            no.direita = self.remover(no.direita, no.valor)
        return no

    def valor_minimo(self, no):
        atual = no
        while atual.esquerda:
            atual = atual.esquerda
        return atual.valor

    def altura(self, no):
        if no is None:
            return 0
        altura_esquerda = self.altura(no.esquerda)
        altura_direita = self.altura(no.direita)
        return max(altura_esquerda, altura_direita) + 1

    def esta_balanceada(self, no):
        if no is None:
            return True
        altura_esquerda = self.altura(no.esquerda)
        altura_direita = self.altura(no.direita)
        return abs(altura_esquerda - altura_direita) <= 1 and self.esta_balanceada(no.esquerda) and self.esta_balanceada(no.direita)

def main():
    abb = ArvoreBinariaBusca()

    while True:
        print("\nMenu:")
        print("1. Criar Árvore")
        print("2. Exibir Árvore")
        print("3. Buscar")
        print("4. Inserir")
        print("5. Remover")
        print("6. Verificar se está balanceada")
        print("0. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue

        if opcao == 1:
            abb.criar_arvore()
        elif opcao == 2:
            if abb.raiz is None:
                print("A árvore está vazia.")
            else:
                print("Árvore: ", end="")
                abb.exibir_arvore(abb.raiz)
                print()
        elif opcao == 3:
            valor = int(input("Digite o valor a ser buscado: "))
            encontrado = abb.buscar(abb.raiz, valor)
            print("Valor encontrado." if encontrado else "Valor não encontrado.")
        elif opcao == 4:
            valor = int(input("Digite o valor a ser inserido: "))
            abb.raiz = abb.inserir(abb.raiz, valor)
            print("Valor inserido.")
        elif opcao == 5:
            if abb.raiz is None:
                print("A árvore está vazia, nada para remover.")
            else:
                valor = int(input("Digite o valor a ser removido: "))
                abb.raiz = abb.remover(abb.raiz, valor)
                print("Valor removido.")
        elif opcao == 6:
            if abb.esta_balanceada(abb.raiz):
                print("A árvore está balanceada.")
            else:
                print("A árvore não está balanceada.")
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
