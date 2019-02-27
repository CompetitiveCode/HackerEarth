#Answer to Add two arrays - https://www.hackerearth.com/practice-onboarding/add-two-arrays-1

N = int(input())

# Get the array 
numArray1 = list(map(int, input().split()))
numArray2 = list(map(int, input().split()))

sumArray = numArray1

# Write the logic here:

for i in range(N):
    sumArray[i] += numArray2[i]

# Print the sumArray
for element in sumArray:
    print(element, end=" ")
    
print("")