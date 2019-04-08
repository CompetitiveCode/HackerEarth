#Answer to Count Divisors - https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/count-divisors/

l,r,k = map(int,input().split())
total = 0
for i in range(min(l,r),max(l,r)+1):
    if i%k == 0:
        total += 1
print(total)