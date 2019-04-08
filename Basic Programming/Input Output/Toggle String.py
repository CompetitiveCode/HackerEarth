#Answer to Toggle String - https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/modify-the-string/

for i in input():
    print(i.lower() if i.isupper() else i.upper(),end = "")