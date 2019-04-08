#Answer to Factorial - https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-factorial/

def fac(n):
    if n == 1:
        return 1
    else:
        return fac(n-1) * n

print(fac(int(input())))