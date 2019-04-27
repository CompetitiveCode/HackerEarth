# Answer to Bricks Game
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/bricks-game-5140869d/


n = int(input())
i = 1
while(n > 0):
    if n > i:
        n -= i
    elif n <= i:
        print('Patlu')
        break
    if n > i*2:
        n -= i*2
    elif n <= i*2:
        print('Motu')
        break
    i += 1
