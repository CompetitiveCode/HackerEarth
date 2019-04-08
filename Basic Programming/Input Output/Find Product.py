#Answer to Find Product - https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/

answer = 1
n = int(input())
arr = list(map(int,input().split()))
for i in arr:
    answer = (answer * i) % (10 ** 9 + 7)
print(answer)