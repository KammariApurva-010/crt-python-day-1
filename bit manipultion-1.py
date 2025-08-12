n=int(input())
binaryString=""
while (n!=0):
    rem=n%2
    binaryString+=str(rem)
    n = n//2
print(binaryString[::-1])
