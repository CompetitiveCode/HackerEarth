#Answer to Palindromic String - https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/palindrome-check-2/

string = input()
print("YES" if string == string[::-1] else "NO")