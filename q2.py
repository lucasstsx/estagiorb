def sequencia_fibonacci(n):
    fib_seq = [0, 1]
    # Gerar a sequência de Fibonacci até que o último número seja maior que n
    while fib_seq[-1] < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    print(fib_seq)
    return fib_seq

def esta_na_sequencia_fibonacci(numero):
    # Verificar se o número está na sequência de Fibonacci
    seq_fib = sequencia_fibonacci(numero)
    if numero in seq_fib:
        return True
    else:
        return False

def main():
    try:
        numero = int(input("Informe um número inteiro positivo: "))
        if numero < 0:
            raise ValueError
        if esta_na_sequencia_fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, informe um número inteiro positivo.")

if __name__ == "__main__":
    main()
