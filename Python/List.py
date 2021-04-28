#Sum of the Multiples
list  = [b for b in range(1000) if b%3 == 0 or b%5 == 0]
print(sum(list))