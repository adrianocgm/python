import time

def cronometro(segundos):
    for i in range(segundos, 0, -1):
        print(f"Tempo restante: {i} segundos", end="\r")
        time.sleep(1)
    
    print("Tempo esgotado!")

def main():
    print("Bem-vindo ao Cronômetro!")
    segundos = int(input("Digite a quantidade de segundos para o cronômetro: "))

    cronometro(segundos)

if __name__ == "__main__":
    main()
