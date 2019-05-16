# Answer to Goki and his breakup
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/tds-and-his-breakup/


n, x = int(input()),int(input())
for _ in range(n):
    if int(input()) < x:
        print('NO')
    else:
        print('YES')
