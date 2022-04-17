def linearSearch(vetor, alvo):
  for i in range(len(vetor)):
    if i%100==0: 
      print(f"Interação numero {i}")

    if(vetor[i] == alvo):
      print(f"Valor encontrado no indice {i}")
      return i
  print("Não encontrado")
  return -1


def BuscaBinaria(vetor, meio, inicio, fim, alvo, i):
    i += 1
    print("Interação numero ", i)
    if(inicio > fim):
        print("#########Valor não encontrado#########")
        return -1
    meio = (inicio+fim)//2

    if(vetor[meio] == alvo):
        print(f"********Valor encontrado no indice {meio}*********")
        return meio
    elif(vetor[meio] > alvo):
        return BuscaBinaria(vetor, meio, inicio, meio-1, alvo, i)
    elif(vetor[meio] < alvo):
        return BuscaBinaria(vetor, meio, meio+1, fim, alvo, i)


vetor = []
for i in range(0, 1001):
    vetor.append(i)
inicio = 0
fim = len(vetor)-1
meio = len(vetor)//2
alvo = 500
i = 0


print("___________________________")
print("LINEAR SEARCH")
alvo=500
linearSearch(vetor, alvo)
print("___________________________")
alvo=200
linearSearch(vetor, alvo)
print("___________________________")
alvo=1001
linearSearch(vetor, alvo)


print("___________________________")
print("BINARY SEARCH")
BuscaBinaria(vetor, meio, inicio, fim, alvo, i)
print("___________________________")
alvo = 200
BuscaBinaria(vetor, meio, inicio, fim, alvo, i)
print("___________________________")
alvo = 1001
BuscaBinaria(vetor, meio, inicio, fim, alvo, i)