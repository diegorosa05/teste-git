def fibonacci(num):
    sequence = [0, 1]
    while sequence[-1] < num:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    if num in sequence:
        print(f'O número {num} pertence à sequência de Fibonacci.')
    else:
        print(f'O número {num} não pertence à sequência de Fibonacci.')

fibonacci(21)
