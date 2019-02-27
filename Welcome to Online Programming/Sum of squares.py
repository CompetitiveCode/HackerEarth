#Answer to Sum of squares - https://www.hackerearth.com/practice-onboarding/sum-of-squares-1

N = input()

# Get the input
numArray = map(int, input().split())

sum_integer = sum(i**2 for i in numArray)
# Write the logic to add these numbers here

# Print the sum
print(sum_integer)