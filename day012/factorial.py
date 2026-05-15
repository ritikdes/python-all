import time

# Factorial recursively
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)

# Factorial iteratively
def factorial_iteratively(n):
    fact = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2, n+1):
            fact = fact * i
        return fact
        
start_rec = time.time()
fact_re = factorial_recursive(20)
rec_time = time.time()
total_time = rec_time - start_rec
print(f"Factorial recursively: {fact_re} with time: {total_time:.6f}")

start_ite = time.time()
fact_ite = factorial_iteratively(20)
ite_time = time.time()
itr_time = ite_time - start_ite
print(f"Factorial iteratively: {fact_ite} with time: {itr_time:.6f}")