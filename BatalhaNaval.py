from random import randint

borda = []

for x in range(10):
    borda.append(["\033[1;36mO"] * 10)

def print_borda(borda):
    for linha in borda:
        print(" ".join(linha))

print("\nJogo Batalha Naval!\n")
print_borda(borda)

def linha_aleatoria(borda):
    return randint(0, len(borda) - 1)

def coluna_aleatoria(borda):
    return randint(0, len(borda[0]) - 1)

navio_linha = linha_aleatoria(borda)
navio_coluna = coluna_aleatoria(borda)

for turn in range(10):
    linha = int(input("\nEscolha uma linha para jogar: "))
    coluna = int(input("\nEscolha uma coluna para jogar: "))

    if coluna == linha and coluna == coluna:
        print("\nParabéns Apedeuta! Você afundou um navio!")
        break

    else:
        if (linha < 0 or linha > 10) or (coluna < 0 or coluna > 10):
            print("\nEssa cassa não está no oceano!")

        elif(borda[linha][coluna] == "X"):
            print("\nApedeuta, o objetivo é encontrar navios escondidos! Esse você já achou!")

        else:
            print("\nParabens Apedeuta, encontrastes um navio!")
            borda[linha][coluna] = "X"

        print (turn + 1)
        print_borda(borda)

        if turn > 10:
            print("\nApedeutinha ainda tem muito a aprender, você perdeu!")

print("\nA localização do navio é", navio_linha)
print(navio_coluna)