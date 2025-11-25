par = impar = 0

while True:
    try:
        n = int(input("Digite um valor (0 para sair): "))
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")
        continue

    if n == 0:
        break
    par += (n % 2 == 0)
    impar += (n % 2 != 0)

print(f"Pares: {par} | Ímpares: {impar}")
