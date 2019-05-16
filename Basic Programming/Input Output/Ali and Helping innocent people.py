# Answer to Ali and Helping innocent people
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cartag-948c2b02


tag = input()
if (int(tag[0])+int(tag[1]))%2 == 0 and (int(tag[3])+int(tag[4]))%2 == 0 and (int(tag[4])+int(tag[5]))%2 == 0 and (int(tag[7])+int(tag[8]))%2 == 0 and tag[2] not in 'AEIOUY':
    print('valid')
else:
    print('invalid')
