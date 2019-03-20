#Answer to Prime Number - https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/prime-number-8/

num = int(input())

def prime(n):
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0: 
        return False
    
    i = 5
    while(i * i <= n) : 
        if n % i == 0 or n % (i + 2) == 0: 
            return False
        i += 6

    return True 
  
for i in range(2, num + 1): 
    if prime(i): 
        print(i, end =" ")