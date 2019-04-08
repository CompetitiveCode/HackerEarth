#Answer to Roy and Profile Picture - https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/roy-and-profile-picture/

l = int(input())
for _ in range(int(input())):
    w,h = map(int, input().split())
    if w < l or h < l:
        print("UPLOAD ANOTHER")
    elif w != h:
        print("CROP IT")
    else:
        print("ACCEPTED")