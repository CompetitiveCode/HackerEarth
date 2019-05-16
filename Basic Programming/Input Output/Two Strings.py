# Answer to Two Strings
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/two-strings-4/


for _ in range(int(input())):
    a, b = map(str, input().split())
    if sorted(a) == sorted(b):
        print('YES')
    else:
        print('NO')
