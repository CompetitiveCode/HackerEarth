# Answer to Duration
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/duration/


for _ in range(int(input())):
    sh, sm, eh, em = map(int, input().split())
    minute = em+60-sm
    hour = eh-sh-1+(minute//60)
    print(hour,minute%60)
