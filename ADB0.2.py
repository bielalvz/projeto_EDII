# Classe para representar um nó da árvore binária
class No:
    def __init__(self, valor):
        # Inicializa um nó com o valor dado e filhos à esquerda e à direita como None
        self.valor = valor
        self.esquerda = None
        self.direita = None

# Classe para gerenciar a Árvore Binária de Busca (ABB)
class ArvoreBinariaBusca:
    def __init__(self):
        # Inicializa a árvore com a raiz como None
        self.raiz = None

    def criar_arvore(self):
        # Reseta a árvore, tornando-a vazia
        self.raiz = None
        print("Árvore criada!")

    def exibir_arvore(self, no):
        # Percorre a árvore em ordem (esquerda, raiz, direita) e exibe os valores
        if no:
            self.exibir_arvore(no.esquerda)  # Percorre a subárvore esquerda
            print(no.valor, end=" ")        # Exibe o valor do nó atual
            self.exibir_arvore(no.direita)  # Percorre a subárvore direita

    def buscar(self, no, valor):
        # Busca um valor na árvore recursivamente
        if no is None or no.valor == valor:
            return no  # Retorna o nó encontrado ou None se não existir
        if valor < no.valor:
            return self.buscar(no.esquerda, valor)  # Busca na subárvore esquerda
        return self.buscar(no.direita, valor)       # Busca na subárvore direita

    def inserir(self, no, valor):
        # Insere um valor na árvore recursivamente
        if no is None:
            return No(valor)  # Cria e retorna um novo nó
        if valor < no.valor:
            no.esquerda = self.inserir(no.esquerda, valor)  # Insere na subárvore esquerda
        elif valor > no.valor:
            no.direita = self.inserir(no.direita, valor)    # Insere na subárvore direita
        return no  # Retorna o nó atualizado

    def remover(self, no, valor):
        # Remove um valor da árvore recursivamente
        if no is None:
            return no  # Valor não encontrado
        if valor < no.valor:
            no.esquerda = self.remover(no.esquerda, valor)  # Remove na subárvore esquerda
        elif valor > no.valor:
            no.direita = self.remover(no.direita, valor)    # Remove na subárvore direita
        else:
            # Caso o nó tenha um ou nenhum filho
            if no.esquerda is None:
                return no.direita
            elif no.direita is None:
                return no.esquerda
            # Caso o nó tenha dois filhos, substitui pelo menor valor da subárvore direita
            no.valor = self.valor_minimo(no.direita)
            no.direita = self.remover(no.direita, no.valor)
        return no

    def valor_minimo(self, no):
        # Encontra o menor valor na subárvore
        atual = no
        while atual.esquerda:
            atual = atual.esquerda  # Move-se sempre para a esquerda
        return atual.valor

    def altura(self, no):
        # Calcula a altura de um nó recursivamente
        if no is None:
            return 0
        altura_esquerda = self.altura(no.esquerda)
        altura_direita = self.altura(no.direita)
        return max(altura_esquerda, altura_direita) + 1

    def esta_balanceada(self, no):
        # Verifica se a árvore está balanceada
        if no is None:
            return True
        altura_esquerda = self.altura(no.esquerda)
        altura_direita = self.altura(no.direita)
        # Verifica se as alturas das subárvores diferem em no máximo 1
        return abs(altura_esquerda - altura_direita) <= 1 and \
               self.esta_balanceada(no.esquerda) and \
               self.esta_balanceada(no.direita)

# Função principal que implementa o menu de interação
def main():
    abb = ArvoreBinariaBusca()  # Cria uma nova árvore

    while True:
        # Menu de opções
        print("\nMenu:")
        print("1. Criar Árvore")
        print("2. Exibir Árvore")
        print("3. Buscar")
        print("4. Inserir")
        print("5. Remover")
        print("6. Verificar se está balanceada")
        print("0. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))  # Captura a opção escolhida
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue

        if opcao == 1:
            abb.criar_arvore()  # Reseta a árvore
        elif opcao == 2:
            if abb.raiz is None:
                print("A árvore está vazia.")  # Verifica se a árvore está vazia
            else:
                print("Árvore: ", end="")
                abb.exibir_arvore(abb.raiz)  # Exibe os valores da árvore
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

# Executa o programa
if __name__ == "__main__":
    main()
