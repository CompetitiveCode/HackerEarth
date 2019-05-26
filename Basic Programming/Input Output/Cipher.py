# Answer to Cipher
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cipher-1/


text, res, num = input(), '', int(input())
for i in text:
    if i.isalpha():
        temp = ord(i)+(num%26)
        temp1, temp2 = temp+1, 0
        if ord(i) > 64 and ord(i) < 91:
            if temp > 90:
                temp1, temp2 = 90, 64
        else:
            if temp > 122:
                temp1, temp2 = 122, 96
        res += chr((temp%temp1)+temp2)
    elif i.isnumeric():
        res += str((int(i)+num)%10)
    else:
        res += i
print(res)
