#Answer to Range of Integers - https://www.hackerearth.com/practice-onboarding/range-of-integers-1

# Get L and R from the input
L, R = map(int, input().split())
for i in range(L,R+1):
    print(i,end=" ")
# Write here the logic to print all integers between L and R