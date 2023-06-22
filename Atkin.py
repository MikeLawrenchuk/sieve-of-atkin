def sieve_of_atkin(limit):
    P = [2,3]
    sieve=[False]*(limit+1)
    for x in range(1,int(limit**0.5)+1):
        for y in range(1,int(limit**0.5)+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7 : sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
    for n in range(5,int(limit**0.5)):
        if sieve[n]:
            for k in range(n**2,limit+1,n**2):
                sieve[k] = False
    for n in range(5,limit):
        if sieve[n]: P.append(n)
    return P

def count_twin_primes(primes):
    twin_primes_count = 0
    for i in range(1, len(primes)):
        if primes[i] - primes[i - 1] == 2:
            twin_primes_count += 1
    return twin_primes_count

limit = 32452843
primes = sieve_of_atkin(limit)
twin_primes_count = count_twin_primes(primes)

print("Number of twin primes between 1 and", limit, ":", twin_primes_count)
