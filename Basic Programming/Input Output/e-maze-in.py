# Answer to e-maze-in
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/e-maze-in-1aa4e2ac/


x,y=0, 0
for i in input():
    if i == 'L':x-=1
    if i == 'R':x+=1
    if i == 'U':y+=1
    if i == 'D':y-=1
print(x, y)
