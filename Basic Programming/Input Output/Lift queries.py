# Answer to Lift queries
# https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/lift-queries


A, B = 0, 7
for _ in range(int(input())):
    n = int(input())
    if abs(n-A) < abs(n-B):
        A = n
    elif abs(n-A) > abs(n-B):
        B = n
    elif A < B:
        A = n
    else:
        B = n
    print('A' if A == n else 'B')
