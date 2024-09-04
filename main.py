def is_in_fibonacci(num:int) -> int:
	sequence = [0, 1]
	while True:
		i = len(sequence)
		accumulator = sequence[i-2] + sequence[i-1]
		sequence.append(accumulator)
		if accumulator == num:
			return i
		if accumulator > num:
			return

if __name__ == "__main__":
	while True:
		option = int(input("insira um numero inteiro\n"))
		result = is_in_fibonacci(option)
		if result is not None:
			print(f"O numero {option} se encontra na posição {result} da sequencia de Fibonacci\n\n")
		else:
			print(f"O numero {option} não se encontra na sequencia de Fibonacci\n\n")