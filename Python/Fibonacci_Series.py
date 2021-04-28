# Fibonacci Series

def Fib(n):
    numbers = [0, 1]
    if numbers[-1] < n:
        return numbers.append(numbers[-1] + numbers[-2])

    return numbers

def Sum(n):
    a = Sum(n)
    b = [t fir t in range Fib if t%2 == 0]
    return b

result = Sum(400000)