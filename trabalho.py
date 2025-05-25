import random
import timeit
import matplotlib.pyplot as plt


# Funções
def insertion_sort(vetor):
    size = len(vetor)

    for i in range(1, size):
        key = vetor[i]
        j = i - 1

        while j >= 0 and vetor[j] > key:
            vetor[j + 1] = vetor[j]
            j -= 1

        vetor[j + 1] = key


def partition(vetor, low, high):
    i = low - 1
    pivot = vetor[high]

    for j in range(low, high):
        if vetor[j] <= pivot:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]

    vetor[i + 1], vetor[high] = vetor[high], vetor[i + 1]
    return i + 1


def quick_sort(vetor, low, high):
    while low < high:
        pivot_index = partition(vetor, low, high)

        if pivot_index - low < high - pivot_index:
            quick_sort(vetor, low, pivot_index - 1)
            low = pivot_index + 1
        else:
            quick_sort(vetor, pivot_index + 1, high)
            high = pivot_index - 1


# Declaração dos tamanhos
Tamanhos = [50, 500, 5000, 50000]

TempoCrescenteQuickSort = []
TempoDecrescenteQuickSort = []
TempoAleatorioQuickSort = []

TempoCrescenteInsertionSort = []
TempoDecrescenteInsertionSort = []
TempoAleatorioInsertionSort = []


for tamanho in Tamanhos:

    VetCrescenteQuickSort = list(range(tamanho))
    VetCrescenteInsertionSort = list(range(tamanho))

    tempo_execucao = timeit.timeit(lambda: quick_sort(VetCrescenteQuickSort, 0, len(VetCrescenteQuickSort) - 1), number=1)
    TempoCrescenteQuickSort.append(tempo_execucao)
    print(f"Tempo de execução do Quick Sort para vetor crescente ({tamanho} elementos): {tempo_execucao} segundos")

    tempo_execucao = timeit.timeit(lambda: insertion_sort(VetCrescenteInsertionSort), number=1)
    TempoCrescenteInsertionSort.append(tempo_execucao)
    print(f"Tempo de execução do Insertion Sort para vetor crescente ({tamanho} elementos): {tempo_execucao} segundos")


    VetDecrescenteQuickSort = list(range(tamanho, 0, -1))
    VetDecrescenteInsertionSort = list(range(tamanho, 0, -1))

    tempo_execucao = timeit.timeit(lambda: quick_sort(VetDecrescenteQuickSort, 0, len(VetDecrescenteQuickSort) - 1), number=1)
    TempoDecrescenteQuickSort.append(tempo_execucao)
    print(f"Tempo de execução do Quick Sort para vetor decrescente ({tamanho} elementos): {tempo_execucao} segundos")

    tempo_execucao = timeit.timeit(lambda: insertion_sort(VetDecrescenteInsertionSort), number=1)
    TempoDecrescenteInsertionSort.append(tempo_execucao)
    print(f"Tempo de execução do Insertion Sort para vetor decrescente ({tamanho} elementos): {tempo_execucao} segundos")


    VetAleatorioQuickSort = random.sample(range(tamanho), tamanho)
    VetAleatorioInsertionSort = random.sample(range(tamanho), tamanho)

    tempo_execucao = timeit.timeit(lambda: quick_sort(VetAleatorioQuickSort, 0, len(VetAleatorioQuickSort) - 1), number=1)
    TempoAleatorioQuickSort.append(tempo_execucao)
    print(f"Tempo de execução do Quick Sort para vetor aleatório ({tamanho} elementos): {tempo_execucao} segundos")

    tempo_execucao = timeit.timeit(lambda: insertion_sort(VetAleatorioInsertionSort), number=1)
    TempoAleatorioInsertionSort.append(tempo_execucao)
    print(f"Tempo de execução do Insertion Sort para vetor aleatório ({tamanho} elementos): {tempo_execucao} segundos")
    print()


# Plotando os gráficos
plt.plot(Tamanhos, TempoCrescenteQuickSort, label='Quick Sort', color='Blue', marker='*')
plt.plot(Tamanhos, TempoCrescenteInsertionSort, label='Insertion Sort', color='Red', marker='*')
plt.ylabel('Tempo em Segundos')
plt.xlabel('Tamanho do vetor')
plt.title('Comparação do Vetor Crescente')
plt.legend()
plt.show()

plt.plot(Tamanhos, TempoDecrescenteQuickSort, label='Quick Sort', color='Blue', marker='*')
plt.plot(Tamanhos, TempoDecrescenteInsertionSort, label='Insertion Sort', color='Red', marker='*')
plt.ylabel('Tempo em Segundos')
plt.xlabel('Tamanho do vetor')
plt.title('Comparação do Vetor Decrescente')
plt.legend()
plt.show()

plt.plot(Tamanhos, TempoAleatorioQuickSort, label='Quick Sort', color='Blue', marker='*')
plt.plot(Tamanhos, TempoAleatorioInsertionSort, label='Insertion Sort', color='Red', marker='*')
plt.ylabel('Tempo em Segundos')
plt.xlabel('Tamanho do vetor')
plt.title('Comparação do Vetor Aleatório')
plt.legend()
plt.show()