# Answer to Book of Potion making
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/sum-it-if-you-can-4867f851/


n = input()
res, j = 0, 1
for i in n:
    res += int(i)*j
    j += 1
print('Legal ISBN' if res%11 == 0 else 'Illegal ISBN')
