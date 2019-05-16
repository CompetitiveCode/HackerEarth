# Answer to Aman & Mr.Sharma
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/aman-mrsharma/


res = 0
for _ in range(int(input())):
    r, x = map(int,input().split())
    if 2*22*r/7 < x*100:
        res += 1
print(res)
