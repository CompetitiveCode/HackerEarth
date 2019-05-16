# Answer to Anagrams
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/anagrams-651


for _ in range(int(input())):
    a,b = input(),input()
    alpha = [0] * 26
    for i in a:
        alpha[ord(i)-ord('a')] += 1
    for i in b:
        alpha[ord(i)-ord('a')] -= 1
    print(sum(map(abs,alpha)))
