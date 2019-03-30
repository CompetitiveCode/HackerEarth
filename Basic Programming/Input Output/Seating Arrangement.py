#Answer to Seating Arrangement - https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seating-arrangement-1/

addi = {5:3,4:5,3:7,2:9,1:11} #This is for the left side. If a number%6 is this, then we have to add this.
subi = {5:9,4:7,3:5,2:3,1:1} #This is for the right side. If a number%6 is this, then we have to subtract this.

for _ in range(int(input())): #Runs for T test cases
    n = int(input()) #To get the number to be checked.
    seat = "" #This is to store the seat type
    opp = 0 #This is to store which seat would be opposite to them
    
    #First getting which type of seat
    if n%6 == 0 or n%6 == 1: #If a number % 6 gives 1 or 0, then it is a Window Seat
        seat = " WS"
    elif n%3 == 0 or n%3 == 1: #If a number % 3 gives 1 or 0, then it is a Aisle Seat
        seat = " AS"
    else: #If none of the above case, then it is a Middle Seat
        seat = " MS"

    #Now getting which is the opposite seat
    if n//6 == n/6: #If 6 is a perfect divisor, that means it is a special case
        if (n/6)%2 == 1: #If that perfect divisor%2 is 1, then we should just add a number to it.
            opp = n+1
        else: #If it results a 0, then we should subtract 12 and add 1, or simply subtract 11.
            opp = n - 12 + 1
    elif (n//6) % 2 == 0: #If 6 is not a perfect divisor, then we check if the result of n//6 is even.
        opp = n + addi[n%6] #If it is, that means, it is in left side and we use the addi dictionary
    else: #If it is odd, then the seat is on the right side
        opp = n - subi[n%6] #That means we will be using the subi dictionary
    print(str(opp)+seat) #Finally we use the two results and print it.