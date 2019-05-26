# Answer to Prime Minister's number
# https://www.hackerearth.com/practice/basic-programming/complexity-analysis/time-and-space-complexity/practice-problems/algorithm/prime-ministers-number/


from math import sqrt

primes = [2,3]

def prime(num):
    if num in primes:
        return True
    elif num <= 1:
        return False
    elif num%2 == 0 or num%3 == 0:
        return False
    else:
        i = 5
        while(i * i <= num) : 
            if (num % i == 0 or num % (i + 2) == 0) : 
                return False
            i = i + 6
        return True

lower, upper = map(int, input().split())
res = []
for num in range(lower,upper + 1):
    if prime(num):
        if prime(sum(int(i) for i in str(num))):
            res.append(str(num))
print(' '.join(res))
